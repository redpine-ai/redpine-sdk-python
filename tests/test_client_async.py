import json

import httpx
import pytest
import respx

from redpine import AsyncRedpine, QuotaExceeded
from redpine.client import DEFAULT_BASE_URL

KEY = "sk_test_fake_abc123"
SEARCH_OK = {"results": [], "queryId": "q-1", "latencyMs": 1}


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for v in ("REDPINE_API_KEY", "CONNECT_API_KEY", "REDPINE_BASE_URL"):
        monkeypatch.delenv(v, raising=False)


@respx.mock
async def test_async_search():
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(
        return_value=httpx.Response(200, json=SEARCH_OK)
    )
    async with AsyncRedpine(KEY) as c:
        r = await c.search("q", collection="c")
    assert r.query_id == "q-1"
    assert json.loads(route.calls.last.request.content)["collection"] == "c"


@respx.mock
async def test_async_retry_then_raise(monkeypatch):
    slept = []

    async def fake_sleep(s):
        slept.append(s)

    monkeypatch.setattr("redpine.client.asyncio.sleep", fake_sleep)
    route = respx.get(f"{DEFAULT_BASE_URL}/api/v1/search/quota").mock(
        return_value=httpx.Response(429, json={"error": {"code": "RATE_LIMITED", "message": "m"}})
    )
    async with AsyncRedpine(KEY, max_retries=1) as c:
        with pytest.raises(QuotaExceeded):
            await c.quota()
    assert route.call_count == 2 and len(slept) == 1


@respx.mock
async def test_async_assisted_search_waits_longer_by_default():
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/assisted").mock(
        return_value=httpx.Response(
            200,
            json={
                "status": "no_relevant_results",
                "queryUnderstanding": {},
                "billing": {"chargedResults": 0, "tokensCharged": 0},
                "queryId": "q-4",
                "latencyMs": 1,
                "iterationsRun": 1,
            },
        )
    )
    async with AsyncRedpine(KEY) as c:
        r = await c.assisted_search("q", collection="c")
    assert r.status == "no_relevant_results"
    assert route.calls.last.request.extensions["timeout"]["read"] == 120.0
