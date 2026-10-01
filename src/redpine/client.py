"""Hand-written client over the generated core.

Configuration is deliberately small: api key (arg or env), timeout, max_retries.
The base URL is not a parameter — it is https://api.redpine.ai unless the
REDPINE_BASE_URL environment variable says otherwise (used for staging smoke
tests and local mocks; not part of the documented surface).
"""

from __future__ import annotations

import asyncio
import os
import time
from typing import Any

from typing_extensions import Self

from ._generated.api.search import (
    get_cached_result,
    get_quota,
    list_collections,
    search_assisted,
    search_collection,
    search_preview,
    search_query,
    search_unlock,
)
from ._generated.client import AuthenticatedClient
from ._generated.models import (
    AssistedSearchRequest,
    AssistedSearchResponse,
    CollectionsResponse,
    PreviewUnlockResponse,
    QuotaInfo,
    SearchCollectionBody,
    SearchPreviewRequest,
    SearchRequest,
    SearchResponse,
    SearchResultsPreviewResponse,
    UnlockRequest,
)
from ._generated.models.assisted_search_request_filters_type_0 import (
    AssistedSearchRequestFiltersType0,
)
from ._generated.models.search_collection_body_filters_type_0 import (
    SearchCollectionBodyFiltersType0,
)
from ._generated.models.search_preview_request_filters_type_0 import (
    SearchPreviewRequestFiltersType0,
)
from ._generated.models.search_request_filters_type_0 import SearchRequestFiltersType0
from ._generated.types import UNSET, Response
from ._retry import backoff_seconds, should_retry
from .errors import AuthError, QuotaExceeded, error_from_response
from .filters import Filter, to_filter_dict

DEFAULT_BASE_URL = "https://api.redpine.ai"
ENV_API_KEY = "REDPINE_API_KEY"
ENV_API_KEY_FALLBACK = "CONNECT_API_KEY"
ENV_BASE_URL = "REDPINE_BASE_URL"


def resolve_api_key(explicit: str | None) -> str:
    key = explicit or os.environ.get(ENV_API_KEY) or os.environ.get(ENV_API_KEY_FALLBACK)
    if not key:
        raise AuthError(
            401,
            f"no API key: pass api_key=... or set {ENV_API_KEY} "
            f"(created in the Redpine dashboard under Settings > API Keys)",
        )
    return key


def resolve_base_url() -> str:
    v = os.environ.get(ENV_BASE_URL)
    if v is None:
        return DEFAULT_BASE_URL
    trimmed = v.rstrip("/")
    if not trimmed:
        raise ValueError(f"{ENV_BASE_URL} is set but empty")
    return trimmed


def _one_target(collection: str | None, collections: list[str] | None) -> None:
    has_collections = bool(collections)
    if (collection is None) == (not has_collections):
        raise ValueError("pass exactly one of collection= or collections=")


def _search_body(
    query: str,
    collection: str | None,
    collections: list[str] | None,
    limit: int,
    filters: Filter | dict | None,
    include_metadata: bool,
    include_figures: bool,
) -> SearchRequest:
    _one_target(collection, collections)
    d = to_filter_dict(filters)
    body = SearchRequest(
        query=query,
        limit=limit,
        include_metadata=include_metadata,
        include_figures=include_figures,
    )
    if collection is not None:
        body.collection = collection
    if collections:
        body.collections = list(collections)
    if d is not None:
        body.filters = SearchRequestFiltersType0.from_dict(d)
    return body


class Redpine:
    """Synchronous client. `with Redpine() as c:` or call `close()` when done."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        timeout: float = 30.0,
        max_retries: int = 2,
    ) -> None:
        self._max_retries = max_retries
        self._client = AuthenticatedClient(
            base_url=resolve_base_url(),
            token=resolve_api_key(api_key),
            timeout=timeout,
            raise_on_unexpected_status=False,
        )

    # --- lifecycle -----------------------------------------------------------

    def close(self) -> None:
        self._client.get_httpx_client().close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    # --- core call with retry -----------------------------------------------

    def _call(self, fn, *args: Any, **kwargs: Any):
        attempt = 0
        while True:
            resp: Response = fn(*args, client=self._client, **kwargs)
            if 200 <= resp.status_code < 300:
                return resp.parsed
            if should_retry(resp.status_code, attempt, self._max_retries):
                err = error_from_response(resp.status_code, resp.content, resp.headers)
                retry_after = err.retry_after if isinstance(err, QuotaExceeded) else None
                time.sleep(backoff_seconds(attempt, retry_after))
                attempt += 1
                continue
            raise error_from_response(resp.status_code, resp.content, resp.headers)

    # --- public surface -----------------------------------------------------

    def search(
        self,
        query: str,
        *,
        collection: str | None = None,
        collections: list[str] | None = None,
        limit: int = 10,
        filters: Filter | dict | None = None,
        include_metadata: bool = True,
        include_figures: bool = False,
    ) -> SearchResponse:
        body = _search_body(
            query, collection, collections, limit, filters, include_metadata, include_figures
        )
        return self._call(search_query.sync_detailed, body=body)

    def search_collection(
        self,
        collection: str,
        query: str,
        *,
        limit: int = 10,
        filters: Filter | dict | None = None,
        include_metadata: bool = True,
        include_figures: bool = False,
    ) -> SearchResponse:
        body = SearchCollectionBody(
            query=query,
            limit=limit,
            include_metadata=include_metadata,
            include_figures=include_figures,
        )
        d = to_filter_dict(filters)
        if d is not None:
            body.filters = SearchCollectionBodyFiltersType0.from_dict(d)
        return self._call(search_collection.sync_detailed, collection, body=body)

    def assisted_search(
        self,
        query: str,
        *,
        collection: str | None = None,
        collections: list[str] | None = None,
        limit: int = 10,
        filters: Filter | dict | None = None,
        allow_clarification: bool = True,
        include_metadata: bool = True,
    ) -> AssistedSearchResponse:
        _one_target(collection, collections)
        body = AssistedSearchRequest(
            query=query,
            limit=limit,
            allow_clarification=allow_clarification,
            include_metadata=include_metadata,
        )
        if collection is not None:
            body.collection = collection
        if collections:
            body.collections = list(collections)
        d = to_filter_dict(filters)
        if d is not None:
            body.filters = AssistedSearchRequestFiltersType0.from_dict(d)
        return self._call(search_assisted.sync_detailed, body=body)

    def preview(
        self,
        query: str,
        *,
        collection: str | None = None,
        collections: list[str] | None = None,
        limit: int = 10,
        filters: Filter | dict | None = None,
    ) -> PreviewUnlockResponse:
        """Free: teaser rows plus the cost to unlock each. Never charged, never a quota slot."""
        body = _preview_body(query, collection, collections, limit, filters)
        return self._call(search_preview.sync_detailed, body=body)

    def unlock(
        self,
        query_id: str,
        *,
        result_ids: list[str] | None = None,
    ) -> PreviewUnlockResponse:
        """Pay for previewed rows. `result_ids=None` unlocks every row; re-sending paid ids is free."""
        return self._call(search_unlock.sync_detailed, body=_unlock_body(query_id, result_ids))

    def get_results(self, query_id: str) -> SearchResultsPreviewResponse:
        return self._call(get_cached_result.sync_detailed, query_id, **_NO_IMAGE_DEFAULTS)

    def quota(self) -> QuotaInfo:
        return self._call(get_quota.sync_detailed)

    def collections(self) -> CollectionsResponse:
        return self._call(list_collections.sync_detailed)


def _preview_body(
    query: str,
    collection: str | None,
    collections: list[str] | None,
    limit: int,
    filters: Filter | dict | None,
) -> SearchPreviewRequest:
    _one_target(collection, collections)
    body = SearchPreviewRequest(query=query, limit=limit)
    if collection is not None:
        body.collection = collection
    if collections:
        body.collections = list(collections)
    d = to_filter_dict(filters)
    if d is not None:
        body.filters = SearchPreviewRequestFiltersType0.from_dict(d)
    return body


# get_cached_result's generated kwargs default image options to on (matches UnlockRequest);
# not exposed on get_results yet (matches Go/TS), so suppress them the same way.
_NO_IMAGE_DEFAULTS: dict[str, Any] = {
    "include_figures": UNSET,
    "image_max_width": UNSET,
    "image_max_height": UNSET,
    "image_quality": UNSET,
}


def _unlock_body(query_id: str, result_ids: list[str] | None) -> UnlockRequest:
    # Image options aren't exposed on unlock yet (matches Go/TS) -- suppress the
    # generated model's baked-in defaults so they aren't sent on every call.
    body = UnlockRequest(
        query_id=query_id,
        image_max_height=UNSET,
        image_max_width=UNSET,
        image_quality=UNSET,
        include_figures=UNSET,
    )
    if result_ids is not None:
        body.result_ids = list(result_ids)
    return body


class AsyncRedpine:
    """Asynchronous client. `async with AsyncRedpine() as c:` or `await c.aclose()`."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        timeout: float = 30.0,
        max_retries: int = 2,
    ) -> None:
        self._max_retries = max_retries
        self._client = AuthenticatedClient(
            base_url=resolve_base_url(),
            token=resolve_api_key(api_key),
            timeout=timeout,
            raise_on_unexpected_status=False,
        )

    # --- lifecycle -----------------------------------------------------------

    async def aclose(self) -> None:
        await self._client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()

    # --- core call with retry -----------------------------------------------

    async def _call(self, fn, *args: Any, **kwargs: Any):
        attempt = 0
        while True:
            resp: Response = await fn(*args, client=self._client, **kwargs)
            if 200 <= resp.status_code < 300:
                return resp.parsed
            if should_retry(resp.status_code, attempt, self._max_retries):
                err = error_from_response(resp.status_code, resp.content, resp.headers)
                retry_after = err.retry_after if isinstance(err, QuotaExceeded) else None
                await asyncio.sleep(backoff_seconds(attempt, retry_after))
                attempt += 1
                continue
            raise error_from_response(resp.status_code, resp.content, resp.headers)

    # --- public surface -----------------------------------------------------

    async def search(
        self,
        query: str,
        *,
        collection: str | None = None,
        collections: list[str] | None = None,
        limit: int = 10,
        filters: Filter | dict | None = None,
        include_metadata: bool = True,
        include_figures: bool = False,
    ) -> SearchResponse:
        body = _search_body(
            query, collection, collections, limit, filters, include_metadata, include_figures
        )
        return await self._call(search_query.asyncio_detailed, body=body)

    async def search_collection(
        self,
        collection: str,
        query: str,
        *,
        limit: int = 10,
        filters: Filter | dict | None = None,
        include_metadata: bool = True,
        include_figures: bool = False,
    ) -> SearchResponse:
        body = SearchCollectionBody(
            query=query,
            limit=limit,
            include_metadata=include_metadata,
            include_figures=include_figures,
        )
        d = to_filter_dict(filters)
        if d is not None:
            body.filters = SearchCollectionBodyFiltersType0.from_dict(d)
        return await self._call(search_collection.asyncio_detailed, collection, body=body)

    async def assisted_search(
        self,
        query: str,
        *,
        collection: str | None = None,
        collections: list[str] | None = None,
        limit: int = 10,
        filters: Filter | dict | None = None,
        allow_clarification: bool = True,
        include_metadata: bool = True,
    ) -> AssistedSearchResponse:
        _one_target(collection, collections)
        body = AssistedSearchRequest(
            query=query,
            limit=limit,
            allow_clarification=allow_clarification,
            include_metadata=include_metadata,
        )
        if collection is not None:
            body.collection = collection
        if collections:
            body.collections = list(collections)
        d = to_filter_dict(filters)
        if d is not None:
            body.filters = AssistedSearchRequestFiltersType0.from_dict(d)
        return await self._call(search_assisted.asyncio_detailed, body=body)

    async def preview(
        self,
        query: str,
        *,
        collection: str | None = None,
        collections: list[str] | None = None,
        limit: int = 10,
        filters: Filter | dict | None = None,
    ) -> PreviewUnlockResponse:
        body = _preview_body(query, collection, collections, limit, filters)
        return await self._call(search_preview.asyncio_detailed, body=body)

    async def unlock(
        self,
        query_id: str,
        *,
        result_ids: list[str] | None = None,
    ) -> PreviewUnlockResponse:
        return await self._call(search_unlock.asyncio_detailed, body=_unlock_body(query_id, result_ids))

    async def get_results(self, query_id: str) -> SearchResultsPreviewResponse:
        return await self._call(get_cached_result.asyncio_detailed, query_id, **_NO_IMAGE_DEFAULTS)

    async def quota(self) -> QuotaInfo:
        return await self._call(get_quota.asyncio_detailed)

    async def collections(self) -> CollectionsResponse:
        return await self._call(list_collections.asyncio_detailed)
