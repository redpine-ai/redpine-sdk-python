import json

import pytest

from redpine.errors import (
    AccessDenied,
    AssistedUnavailable,
    AuthError,
    Expired,
    InsufficientCredits,
    NotFound,
    QuotaExceeded,
    RedpineError,
    ValidationError,
    error_from_response,
)


def _body(code="X", message="msg", request_id="req-1"):
    return json.dumps(
        {"error": {"code": code, "message": message, "requestId": request_id}}
    ).encode()


@pytest.mark.parametrize(
    "status,cls",
    [
        (401, AuthError),
        (402, InsufficientCredits),
        (403, AccessDenied),
        (404, NotFound),
        (410, Expired),
        (422, ValidationError),
        (429, QuotaExceeded),
        (503, AssistedUnavailable),
        (500, RedpineError),
        (418, RedpineError),
    ],
)
def test_status_maps_to_class(status, cls):
    err = error_from_response(status, _body())
    assert type(err) is cls
    assert isinstance(err, RedpineError)
    assert err.status == status
    assert err.code == "X"
    assert err.message == "msg"
    assert err.request_id == "req-1"


def test_non_json_body_still_builds_error():
    err = error_from_response(502, b"<html>bad gateway</html>")
    assert type(err) is RedpineError
    assert err.status == 502
    assert err.code is None
    assert "502" in str(err)
    assert err.body is None


def test_quota_exceeded_reads_retry_after():
    err = error_from_response(429, _body("RATE_LIMITED"), {"Retry-After": "7"})
    assert isinstance(err, QuotaExceeded)
    assert err.retry_after == 7.0


def test_quota_exceeded_without_retry_after():
    err = error_from_response(429, _body("RATE_LIMITED"))
    assert err.retry_after is None


def test_str_includes_code_message_and_request_id():
    err = error_from_response(403, _body("FORBIDDEN", "no access", "abc"))
    s = str(err)
    assert "403" in s and "FORBIDDEN" in s and "no access" in s and "abc" in s
