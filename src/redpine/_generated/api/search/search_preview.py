from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.preview_unlock_response import PreviewUnlockResponse
from ...models.search_preview_request import SearchPreviewRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SearchPreviewRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/search/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PreviewUnlockResponse | None:
    if response.status_code == 200:
        response_200 = PreviewUnlockResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PreviewUnlockResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPreviewRequest,
) -> Response[Error | PreviewUnlockResponse]:
    """Preview search results without charging

     Run the same pipeline as POST /api/v1/search/query -- same entitlement checks, same retraction
    filtering, same relevance ranking -- but never charge for it. Every result comes back locked, with a
    teaser snippet in `text` and the cost to unlock it. Works even at a zero balance. Consumes no
    credits, no trial query and no quota.

    Call POST /api/v1/search/unlock with the returned `queryId` to pay for and receive some or all of
    the results in full.

    Args:
        body (SearchPreviewRequest): The result-selection half of SearchRequest. A preview quotes
            results rather than delivering them, so it takes no content-delivery options: figures are
            never fetched (they are not priced into the quote) and metadata is always returned.
            Provide exactly one of `collection` (single) or `collections` (multi).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewUnlockResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPreviewRequest,
) -> Error | PreviewUnlockResponse | None:
    """Preview search results without charging

     Run the same pipeline as POST /api/v1/search/query -- same entitlement checks, same retraction
    filtering, same relevance ranking -- but never charge for it. Every result comes back locked, with a
    teaser snippet in `text` and the cost to unlock it. Works even at a zero balance. Consumes no
    credits, no trial query and no quota.

    Call POST /api/v1/search/unlock with the returned `queryId` to pay for and receive some or all of
    the results in full.

    Args:
        body (SearchPreviewRequest): The result-selection half of SearchRequest. A preview quotes
            results rather than delivering them, so it takes no content-delivery options: figures are
            never fetched (they are not priced into the quote) and metadata is always returned.
            Provide exactly one of `collection` (single) or `collections` (multi).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewUnlockResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPreviewRequest,
) -> Response[Error | PreviewUnlockResponse]:
    """Preview search results without charging

     Run the same pipeline as POST /api/v1/search/query -- same entitlement checks, same retraction
    filtering, same relevance ranking -- but never charge for it. Every result comes back locked, with a
    teaser snippet in `text` and the cost to unlock it. Works even at a zero balance. Consumes no
    credits, no trial query and no quota.

    Call POST /api/v1/search/unlock with the returned `queryId` to pay for and receive some or all of
    the results in full.

    Args:
        body (SearchPreviewRequest): The result-selection half of SearchRequest. A preview quotes
            results rather than delivering them, so it takes no content-delivery options: figures are
            never fetched (they are not priced into the quote) and metadata is always returned.
            Provide exactly one of `collection` (single) or `collections` (multi).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewUnlockResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchPreviewRequest,
) -> Error | PreviewUnlockResponse | None:
    """Preview search results without charging

     Run the same pipeline as POST /api/v1/search/query -- same entitlement checks, same retraction
    filtering, same relevance ranking -- but never charge for it. Every result comes back locked, with a
    teaser snippet in `text` and the cost to unlock it. Works even at a zero balance. Consumes no
    credits, no trial query and no quota.

    Call POST /api/v1/search/unlock with the returned `queryId` to pay for and receive some or all of
    the results in full.

    Args:
        body (SearchPreviewRequest): The result-selection half of SearchRequest. A preview quotes
            results rather than delivering them, so it takes no content-delivery options: figures are
            never fetched (they are not priced into the quote) and metadata is always returned.
            Provide exactly one of `collection` (single) or `collections` (multi).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewUnlockResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
