from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.search_response import SearchResponse
from ...types import Response


def _get_kwargs(
    query_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search/results/{query_id}".format(
            query_id=quote(str(query_id), safe=""),
        ),
    }

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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410

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
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SearchResponse]:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Args:
        query_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResponse]
    """

    kwargs = _get_kwargs(
        query_id=query_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | SearchResponse | None:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Args:
        query_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResponse
    """

    return sync_detailed(
        query_id=query_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | SearchResponse]:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Args:
        query_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResponse]
    """

    kwargs = _get_kwargs(
        query_id=query_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | SearchResponse | None:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Args:
        query_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResponse
    """

    return (
        await asyncio_detailed(
            query_id=query_id,
            client=client,
        )
    ).parsed
