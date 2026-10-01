from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.search_results_preview_response import SearchResultsPreviewResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    query_id: str,
    *,
    include_figures: bool | Unset = False,
    image_max_width: int | Unset = 800,
    image_max_height: int | Unset = 600,
    image_quality: int | Unset = 75,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["includeFigures"] = include_figures

    params["imageMaxWidth"] = image_max_width

    params["imageMaxHeight"] = image_max_height

    params["imageQuality"] = image_quality

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search/results/{query_id}".format(
            query_id=quote(str(query_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SearchResultsPreviewResponse | None:
    if response.status_code == 200:
        response_200 = SearchResultsPreviewResponse.from_dict(response.json())

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
) -> Response[Error | SearchResultsPreviewResponse]:
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
    include_figures: bool | Unset = False,
    image_max_width: int | Unset = 800,
    image_max_height: int | Unset = 600,
    image_quality: int | Unset = 75,
) -> Response[Error | SearchResultsPreviewResponse]:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Each result carries `locked`/`tokens`/`cost`: a result not yet paid for through POST
    /api/v1/search/unlock comes back as a teaser (`locked: true`), never the full text.

    Args:
        query_id (str):
        include_figures (bool | Unset):  Default: False.
        image_max_width (int | Unset):  Default: 800.
        image_max_height (int | Unset):  Default: 600.
        image_quality (int | Unset):  Default: 75.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResultsPreviewResponse]
    """

    kwargs = _get_kwargs(
        query_id=query_id,
        include_figures=include_figures,
        image_max_width=image_max_width,
        image_max_height=image_max_height,
        image_quality=image_quality,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_figures: bool | Unset = False,
    image_max_width: int | Unset = 800,
    image_max_height: int | Unset = 600,
    image_quality: int | Unset = 75,
) -> Error | SearchResultsPreviewResponse | None:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Each result carries `locked`/`tokens`/`cost`: a result not yet paid for through POST
    /api/v1/search/unlock comes back as a teaser (`locked: true`), never the full text.

    Args:
        query_id (str):
        include_figures (bool | Unset):  Default: False.
        image_max_width (int | Unset):  Default: 800.
        image_max_height (int | Unset):  Default: 600.
        image_quality (int | Unset):  Default: 75.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResultsPreviewResponse
    """

    return sync_detailed(
        query_id=query_id,
        client=client,
        include_figures=include_figures,
        image_max_width=image_max_width,
        image_max_height=image_max_height,
        image_quality=image_quality,
    ).parsed


async def asyncio_detailed(
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_figures: bool | Unset = False,
    image_max_width: int | Unset = 800,
    image_max_height: int | Unset = 600,
    image_quality: int | Unset = 75,
) -> Response[Error | SearchResultsPreviewResponse]:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Each result carries `locked`/`tokens`/`cost`: a result not yet paid for through POST
    /api/v1/search/unlock comes back as a teaser (`locked: true`), never the full text.

    Args:
        query_id (str):
        include_figures (bool | Unset):  Default: False.
        image_max_width (int | Unset):  Default: 800.
        image_max_height (int | Unset):  Default: 600.
        image_quality (int | Unset):  Default: 75.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SearchResultsPreviewResponse]
    """

    kwargs = _get_kwargs(
        query_id=query_id,
        include_figures=include_figures,
        image_max_width=image_max_width,
        image_max_height=image_max_height,
        image_quality=image_quality,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    query_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_figures: bool | Unset = False,
    image_max_width: int | Unset = 800,
    image_max_height: int | Unset = 600,
    image_quality: int | Unset = 75,
) -> Error | SearchResultsPreviewResponse | None:
    """Re-fetch cached results

     Retrieve previously returned search results using the queryId from a prior search response. Returns
    the same results without billing. The request must use the same API key that performed the original
    search. Results are available for 7 days.

    Each result carries `locked`/`tokens`/`cost`: a result not yet paid for through POST
    /api/v1/search/unlock comes back as a teaser (`locked: true`), never the full text.

    Args:
        query_id (str):
        include_figures (bool | Unset):  Default: False.
        image_max_width (int | Unset):  Default: 800.
        image_max_height (int | Unset):  Default: 600.
        image_quality (int | Unset):  Default: 75.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SearchResultsPreviewResponse
    """

    return (
        await asyncio_detailed(
            query_id=query_id,
            client=client,
            include_figures=include_figures,
            image_max_width=image_max_width,
            image_max_height=image_max_height,
            image_quality=image_quality,
        )
    ).parsed
