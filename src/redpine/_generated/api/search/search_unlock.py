from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.preview_unlock_response import PreviewUnlockResponse
from ...models.unlock_request import UnlockRequest
from ...types import Response


def _get_kwargs(
    *,
    body: UnlockRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/search/unlock",
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

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())

        return response_402

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())

        return response_410

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
    body: UnlockRequest,
) -> Response[Error | PreviewUnlockResponse]:
    """Pay for previewed results and receive them in full

     Charges only for results not already unlocked by an earlier call against the same `queryId` -- re-
    sending the same ids costs nothing. Omit `resultIds` (or pass `null`) to unlock everything from the
    preview.

    Set `includeFigures` to receive figure images as base64 in `metadata.figures[].image_data`. Images
    are returned for every result unlocked under this `queryId`, including ones unlocked by an earlier
    call -- so re-sending ids you have already paid for is how you fetch images you skipped the first
    time, and it charges nothing. At most 50 images are fetched per call; the ids in `resultIds` (or,
    when it is omitted, the results this call unlocked) get that budget first. Figures are free: they
    are not priced into the token cost, so the flag changes latency and response size and never the
    charge. Use the preview's `figureCount` to decide whether to ask.

    Args:
        body (UnlockRequest):

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
    body: UnlockRequest,
) -> Error | PreviewUnlockResponse | None:
    """Pay for previewed results and receive them in full

     Charges only for results not already unlocked by an earlier call against the same `queryId` -- re-
    sending the same ids costs nothing. Omit `resultIds` (or pass `null`) to unlock everything from the
    preview.

    Set `includeFigures` to receive figure images as base64 in `metadata.figures[].image_data`. Images
    are returned for every result unlocked under this `queryId`, including ones unlocked by an earlier
    call -- so re-sending ids you have already paid for is how you fetch images you skipped the first
    time, and it charges nothing. At most 50 images are fetched per call; the ids in `resultIds` (or,
    when it is omitted, the results this call unlocked) get that budget first. Figures are free: they
    are not priced into the token cost, so the flag changes latency and response size and never the
    charge. Use the preview's `figureCount` to decide whether to ask.

    Args:
        body (UnlockRequest):

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
    body: UnlockRequest,
) -> Response[Error | PreviewUnlockResponse]:
    """Pay for previewed results and receive them in full

     Charges only for results not already unlocked by an earlier call against the same `queryId` -- re-
    sending the same ids costs nothing. Omit `resultIds` (or pass `null`) to unlock everything from the
    preview.

    Set `includeFigures` to receive figure images as base64 in `metadata.figures[].image_data`. Images
    are returned for every result unlocked under this `queryId`, including ones unlocked by an earlier
    call -- so re-sending ids you have already paid for is how you fetch images you skipped the first
    time, and it charges nothing. At most 50 images are fetched per call; the ids in `resultIds` (or,
    when it is omitted, the results this call unlocked) get that budget first. Figures are free: they
    are not priced into the token cost, so the flag changes latency and response size and never the
    charge. Use the preview's `figureCount` to decide whether to ask.

    Args:
        body (UnlockRequest):

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
    body: UnlockRequest,
) -> Error | PreviewUnlockResponse | None:
    """Pay for previewed results and receive them in full

     Charges only for results not already unlocked by an earlier call against the same `queryId` -- re-
    sending the same ids costs nothing. Omit `resultIds` (or pass `null`) to unlock everything from the
    preview.

    Set `includeFigures` to receive figure images as base64 in `metadata.figures[].image_data`. Images
    are returned for every result unlocked under this `queryId`, including ones unlocked by an earlier
    call -- so re-sending ids you have already paid for is how you fetch images you skipped the first
    time, and it charges nothing. At most 50 images are fetched per call; the ids in `resultIds` (or,
    when it is omitted, the results this call unlocked) get that budget first. Figures are free: they
    are not priced into the token cost, so the flag changes latency and response size and never the
    charge. Use the preview's `figureCount` to decide whether to ask.

    Args:
        body (UnlockRequest):

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
