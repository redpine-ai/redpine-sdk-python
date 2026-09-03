from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assisted_search_request import AssistedSearchRequest
from ...models.assisted_search_response import AssistedSearchResponse
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    *,
    body: AssistedSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/search/assisted",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AssistedSearchResponse | Error | None:
    if response.status_code == 200:
        response_200 = AssistedSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

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
) -> Response[AssistedSearchResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AssistedSearchRequest,
) -> Response[AssistedSearchResponse | Error]:
    """Assisted search (verified results only)

     Agentic search: the query is interpreted, one or more internal searches are planned and run, every
    candidate is verified as actually addressing the query, and only verified results are returned.

    **Billing differs from `/search/query`:** only delivered, verified results are charged. A
    clarification request or an honest no-results answer costs nothing. Internal search fan-out and LLM
    tokens are absorbed by Redpine.

    Accepts the same `filters` as `/search/query`, applied to every internal search.

    Args:
        body (AssistedSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssistedSearchResponse | Error]
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
    body: AssistedSearchRequest,
) -> AssistedSearchResponse | Error | None:
    """Assisted search (verified results only)

     Agentic search: the query is interpreted, one or more internal searches are planned and run, every
    candidate is verified as actually addressing the query, and only verified results are returned.

    **Billing differs from `/search/query`:** only delivered, verified results are charged. A
    clarification request or an honest no-results answer costs nothing. Internal search fan-out and LLM
    tokens are absorbed by Redpine.

    Accepts the same `filters` as `/search/query`, applied to every internal search.

    Args:
        body (AssistedSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssistedSearchResponse | Error
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AssistedSearchRequest,
) -> Response[AssistedSearchResponse | Error]:
    """Assisted search (verified results only)

     Agentic search: the query is interpreted, one or more internal searches are planned and run, every
    candidate is verified as actually addressing the query, and only verified results are returned.

    **Billing differs from `/search/query`:** only delivered, verified results are charged. A
    clarification request or an honest no-results answer costs nothing. Internal search fan-out and LLM
    tokens are absorbed by Redpine.

    Accepts the same `filters` as `/search/query`, applied to every internal search.

    Args:
        body (AssistedSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssistedSearchResponse | Error]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: AssistedSearchRequest,
) -> AssistedSearchResponse | Error | None:
    """Assisted search (verified results only)

     Agentic search: the query is interpreted, one or more internal searches are planned and run, every
    candidate is verified as actually addressing the query, and only verified results are returned.

    **Billing differs from `/search/query`:** only delivered, verified results are charged. A
    clarification request or an honest no-results answer costs nothing. Internal search fan-out and LLM
    tokens are absorbed by Redpine.

    Accepts the same `filters` as `/search/query`, applied to every internal search.

    Args:
        body (AssistedSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssistedSearchResponse | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
