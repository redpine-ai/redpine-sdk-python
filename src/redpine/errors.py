"""Typed errors for the Redpine SDK. One class per HTTP status we document."""

from __future__ import annotations

import json
from collections.abc import Mapping


class RedpineError(Exception):
    """Base for every error raised by the SDK on a non-2xx response."""

    status: int
    code: str | None
    message: str
    request_id: str | None
    body: dict | None

    def __init__(
        self,
        status: int,
        message: str,
        *,
        code: str | None = None,
        request_id: str | None = None,
        body: dict | None = None,
    ) -> None:
        self.status = status
        self.code = code
        self.message = message
        self.request_id = request_id
        self.body = body
        parts = [f"HTTP {status}"]
        if code:
            parts.append(code)
        parts.append(message)
        if request_id:
            parts.append(f"(request {request_id})")
        super().__init__(" ".join(parts))


class AuthError(RedpineError):
    """401: missing or invalid API key."""


class AccessDenied(RedpineError):
    """403: key has no access to the requested collection."""


class NotFound(RedpineError):
    """404: collection or queryId not found."""


class ValidationError(RedpineError):
    """422: request rejected (query too long, bad filter, ...)."""


class QuotaExceeded(RedpineError):
    """429: rate or quota limit hit. `retry_after` is seconds, when the server said."""

    retry_after: float | None

    def __init__(self, *args, retry_after: float | None = None, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.retry_after = retry_after


class AssistedUnavailable(RedpineError):
    """503: assisted search temporarily unavailable."""


_BY_STATUS: dict[int, type[RedpineError]] = {
    401: AuthError,
    403: AccessDenied,
    404: NotFound,
    422: ValidationError,
    429: QuotaExceeded,
    503: AssistedUnavailable,
}


def _parse_retry_after(headers: Mapping[str, str] | None) -> float | None:
    if not headers:
        return None
    for k, v in headers.items():
        if k.lower() == "retry-after":
            try:
                return float(v)
            except ValueError:
                return None
    return None


def error_from_response(
    status: int,
    body: bytes | str | None,
    headers: Mapping[str, str] | None = None,
) -> RedpineError:
    """Build the right error class from a non-2xx response."""
    parsed: dict | None = None
    if body:
        try:
            candidate = json.loads(body)
            if isinstance(candidate, dict):
                parsed = candidate
        except (ValueError, TypeError):
            parsed = None
    inner = parsed.get("error") if parsed and isinstance(parsed.get("error"), dict) else {}
    code = inner.get("code")
    message = inner.get("message") or f"request failed with status {status}"
    request_id = inner.get("requestId")
    cls = _BY_STATUS.get(status, RedpineError)
    if cls is QuotaExceeded:
        return QuotaExceeded(
            status,
            message,
            code=code,
            request_id=request_id,
            body=parsed,
            retry_after=_parse_retry_after(headers),
        )
    return cls(status, message, code=code, request_id=request_id, body=parsed)
