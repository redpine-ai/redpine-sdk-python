from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.search_collection_body import SearchCollectionBody
from ...models.search_response import SearchResponse
from ...types import Response


def _get_kwargs(
    collection: str,
    *,
    body: SearchCollectionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/search/{collection}".format(
            collection=quote(str(collection), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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
) -> Response[Error | SearchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchCollectionBody,
) -> Response[Error | SearchResponse]:
    """Search a single collection by name

     Shorthand for POST /api/v1/search/query with the collection named in the path instead of the body.
    Same pipeline, same response shape, one collection per call — use /query's `collections` form to
    search several at once.

    Args:
        collection (str):
        body (SearchCollectionBody): Same knobs as SearchRequest minus `collection`/`collections`
            — the target collection is the path segment, so a `collection` key in the body is
            rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResponse]
    """

    kwargs = _get_kwargs(
        collection=collection,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchCollectionBody,
) -> Error | SearchResponse | None:
    """Search a single collection by name

     Shorthand for POST /api/v1/search/query with the collection named in the path instead of the body.
    Same pipeline, same response shape, one collection per call — use /query's `collections` form to
    search several at once.

    Args:
        collection (str):
        body (SearchCollectionBody): Same knobs as SearchRequest minus `collection`/`collections`
            — the target collection is the path segment, so a `collection` key in the body is
            rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResponse
    """

    return sync_detailed(
        collection=collection,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchCollectionBody,
) -> Response[Error | SearchResponse]:
    """Search a single collection by name

     Shorthand for POST /api/v1/search/query with the collection named in the path instead of the body.
    Same pipeline, same response shape, one collection per call — use /query's `collections` form to
    search several at once.

    Args:
        collection (str):
        body (SearchCollectionBody): Same knobs as SearchRequest minus `collection`/`collections`
            — the target collection is the path segment, so a `collection` key in the body is
            rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResponse]
    """

    kwargs = _get_kwargs(
        collection=collection,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection: str,
    *,
    client: AuthenticatedClient | Client,
    body: SearchCollectionBody,
) -> Error | SearchResponse | None:
    """Search a single collection by name

     Shorthand for POST /api/v1/search/query with the collection named in the path instead of the body.
    Same pipeline, same response shape, one collection per call — use /query's `collections` form to
    search several at once.

    Args:
        collection (str):
        body (SearchCollectionBody): Same knobs as SearchRequest minus `collection`/`collections`
            — the target collection is the path segment, so a `collection` key in the body is
            rejected.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResponse
    """

    return (
        await asyncio_detailed(
            collection=collection,
            client=client,
            body=body,
        )
    ).parsed
