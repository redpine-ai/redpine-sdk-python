from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.discovery_answer import DiscoveryAnswer
from ...models.error import Error
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    topic: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    min_h_index: int | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["topic"] = topic

    params["publisher"] = publisher

    params["min_h_index"] = min_h_index

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/search/collections/{name}/journals".format(
            name=quote(str(name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DiscoveryAnswer | Error | None:
    if response.status_code == 200:
        response_200 = DiscoveryAnswer.from_dict(response.json())

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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DiscoveryAnswer | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    topic: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    min_h_index: int | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[DiscoveryAnswer | Error]:
    """List the journals your key can reach in a collection

     Free. Journals present in your scope of the collection, ranked by h-index (each with its
    journal_metric.impact_factor, an impact factor computed by Redpine from OpenAlex citation data with
    the JIF formula. It is not Clarivate's Journal Impact Factor. Journals that publish many news items,
    letters and editorials (for example BMJ, JAMA, The Lancet) score far below their JCR figure, because
    OpenAlex classifies those items as articles.), or with `topic` by the relevant content each journal
    holds on it. Only journals anchored to the metrics table count as proved; sampled, title-only and
    unresolved entries are reported beside the total. Each journal carries the ISSNs to filter a search
    on.

    Args:
        name (str):
        topic (str | Unset):
        publisher (str | Unset):
        min_h_index (int | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscoveryAnswer | Error]
    """

    kwargs = _get_kwargs(
        name=name,
        topic=topic,
        publisher=publisher,
        min_h_index=min_h_index,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    topic: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    min_h_index: int | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> DiscoveryAnswer | Error | None:
    """List the journals your key can reach in a collection

     Free. Journals present in your scope of the collection, ranked by h-index (each with its
    journal_metric.impact_factor, an impact factor computed by Redpine from OpenAlex citation data with
    the JIF formula. It is not Clarivate's Journal Impact Factor. Journals that publish many news items,
    letters and editorials (for example BMJ, JAMA, The Lancet) score far below their JCR figure, because
    OpenAlex classifies those items as articles.), or with `topic` by the relevant content each journal
    holds on it. Only journals anchored to the metrics table count as proved; sampled, title-only and
    unresolved entries are reported beside the total. Each journal carries the ISSNs to filter a search
    on.

    Args:
        name (str):
        topic (str | Unset):
        publisher (str | Unset):
        min_h_index (int | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscoveryAnswer | Error
    """

    return sync_detailed(
        name=name,
        client=client,
        topic=topic,
        publisher=publisher,
        min_h_index=min_h_index,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    topic: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    min_h_index: int | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> Response[DiscoveryAnswer | Error]:
    """List the journals your key can reach in a collection

     Free. Journals present in your scope of the collection, ranked by h-index (each with its
    journal_metric.impact_factor, an impact factor computed by Redpine from OpenAlex citation data with
    the JIF formula. It is not Clarivate's Journal Impact Factor. Journals that publish many news items,
    letters and editorials (for example BMJ, JAMA, The Lancet) score far below their JCR figure, because
    OpenAlex classifies those items as articles.), or with `topic` by the relevant content each journal
    holds on it. Only journals anchored to the metrics table count as proved; sampled, title-only and
    unresolved entries are reported beside the total. Each journal carries the ISSNs to filter a search
    on.

    Args:
        name (str):
        topic (str | Unset):
        publisher (str | Unset):
        min_h_index (int | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DiscoveryAnswer | Error]
    """

    kwargs = _get_kwargs(
        name=name,
        topic=topic,
        publisher=publisher,
        min_h_index=min_h_index,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient | Client,
    topic: str | Unset = UNSET,
    publisher: str | Unset = UNSET,
    min_h_index: int | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
) -> DiscoveryAnswer | Error | None:
    """List the journals your key can reach in a collection

     Free. Journals present in your scope of the collection, ranked by h-index (each with its
    journal_metric.impact_factor, an impact factor computed by Redpine from OpenAlex citation data with
    the JIF formula. It is not Clarivate's Journal Impact Factor. Journals that publish many news items,
    letters and editorials (for example BMJ, JAMA, The Lancet) score far below their JCR figure, because
    OpenAlex classifies those items as articles.), or with `topic` by the relevant content each journal
    holds on it. Only journals anchored to the metrics table count as proved; sampled, title-only and
    unresolved entries are reported beside the total. Each journal carries the ISSNs to filter a search
    on.

    Args:
        name (str):
        topic (str | Unset):
        publisher (str | Unset):
        min_h_index (int | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DiscoveryAnswer | Error
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            topic=topic,
            publisher=publisher,
            min_h_index=min_h_index,
            limit=limit,
            offset=offset,
        )
    ).parsed
