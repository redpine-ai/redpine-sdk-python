import json

import httpx
import pytest
import respx

from redpine import AccessDenied, AuthError, F, QuotaExceeded, Redpine
from redpine.client import DEFAULT_BASE_URL, resolve_api_key, resolve_base_url

KEY = "sk_test_fake_abc123"
SEARCH_OK = {
    "results": [{"id": "d1", "text": "hello", "metadata": None, "collection": None}],
    "queryId": "q-1",
    "latencyMs": 12,
}

# Every SearchRequest/SearchCollectionBody/AssistedSearchRequest to_dict() always emits
# these schema-defaulted image fields (see search_request.py) in addition to the fields
# a caller sets explicitly.
IMAGE_DEFAULTS = {"imageMaxHeight": 600, "imageMaxWidth": 800, "imageQuality": 75}


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for v in ("REDPINE_API_KEY", "CONNECT_API_KEY", "REDPINE_BASE_URL"):
        monkeypatch.delenv(v, raising=False)


# --- configuration -----------------------------------------------------------


def test_explicit_key_wins(monkeypatch):
    monkeypatch.setenv("REDPINE_API_KEY", "sk_test_fake_env")
    assert resolve_api_key("sk_test_fake_arg") == "sk_test_fake_arg"


def test_env_key_and_fallback(monkeypatch):
    monkeypatch.setenv("CONNECT_API_KEY", "sk_test_fake_connect")
    assert resolve_api_key(None) == "sk_test_fake_connect"
    monkeypatch.setenv("REDPINE_API_KEY", "sk_test_fake_redpine")
    assert resolve_api_key(None) == "sk_test_fake_redpine"


def test_missing_key_raises():
    with pytest.raises(AuthError) as ei:
        Redpine()
    assert "REDPINE_API_KEY" in str(ei.value)


def test_base_url_default_and_env(monkeypatch):
    assert resolve_base_url() == DEFAULT_BASE_URL == "https://api.redpine.ai"
    monkeypatch.setenv("REDPINE_BASE_URL", "http://127.0.0.1:8000/")
    assert resolve_base_url() == "http://127.0.0.1:8000"  # trailing slash stripped


def test_base_url_set_but_empty_raises(monkeypatch):
    monkeypatch.setenv("REDPINE_BASE_URL", "")
    with pytest.raises(ValueError, match="REDPINE_BASE_URL"):
        resolve_base_url()
    monkeypatch.setenv("REDPINE_BASE_URL", "///")  # trims to empty
    with pytest.raises(ValueError, match="REDPINE_BASE_URL"):
        resolve_base_url()


def test_constructor_has_no_base_url_parameter():
    import inspect

    assert "base_url" not in inspect.signature(Redpine.__init__).parameters


# --- requests ---------------------------------------------------------------


@respx.mock
def test_search_sends_bearer_and_body():
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(
        return_value=httpx.Response(200, json=SEARCH_OK)
    )
    c = Redpine(KEY)
    r = c.search(
        "crispr",
        collections=["corpus"],
        limit=5,
        filters=F("issn").eq("1664-302X") | F("issn").eq("1932-6203"),
    )
    assert r.query_id == "q-1"
    assert r.results[0].id == "d1"
    req = route.calls.last.request
    assert req.headers["authorization"] == f"Bearer {KEY}"
    assert json.loads(req.content) == {
        "query": "crispr",
        "collections": ["corpus"],
        "limit": 5,
        "filters": {
            "or": [{"field": "issn", "eq": "1664-302X"}, {"field": "issn", "eq": "1932-6203"}]
        },
        "includeMetadata": True,
        "includeFigures": False,
        **IMAGE_DEFAULTS,
    }


@respx.mock
def test_search_accepts_raw_filter_dict():
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(
        return_value=httpx.Response(200, json=SEARCH_OK)
    )
    Redpine(KEY).search("q", collection="c", filters={"journal": "Nature"})
    assert json.loads(route.calls.last.request.content)["filters"] == {"journal": "Nature"}


@respx.mock
def test_search_collection_uses_path_and_omits_collection_key():
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/corpus").mock(
        return_value=httpx.Response(200, json=SEARCH_OK)
    )
    Redpine(KEY).search_collection("corpus", "q")
    body = json.loads(route.calls.last.request.content)
    assert "collection" not in body and "collections" not in body
    assert body["query"] == "q"


@respx.mock
def test_assisted_search():
    payload = {
        "status": "results",
        "queryUnderstanding": {},
        "results": [],
        "clarification": None,
        "billing": {"chargedResults": 0, "tokensCharged": 0},
        "queryId": "q-2",
        "latencyMs": 5,
        "iterationsRun": 1,
    }
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/assisted").mock(
        return_value=httpx.Response(200, json=payload)
    )
    r = Redpine(KEY).assisted_search("why", collection="corpus", allow_clarification=False)
    assert r.status == "results" and r.query_id == "q-2"
    assert json.loads(route.calls.last.request.content)["allowClarification"] is False


@respx.mock
def test_get_results_quota_collections():
    respx.get(f"{DEFAULT_BASE_URL}/api/v1/search/results/q-1").mock(
        return_value=httpx.Response(200, json=SEARCH_OK)
    )
    respx.get(f"{DEFAULT_BASE_URL}/api/v1/search/quota").mock(
        return_value=httpx.Response(
            200,
            json={
                "dailyLimit": 10,
                "dailyUsed": 1,
                "dailyRemaining": 9,
                "monthlyLimit": 100,
                "monthlyUsed": 1,
                "monthlyRemaining": 99,
            },
        )
    )
    respx.get(f"{DEFAULT_BASE_URL}/api/v1/search/collections").mock(
        return_value=httpx.Response(
            200, json={"collections": [{"name": "corpus", "documentCount": 3}], "count": 1}
        )
    )
    c = Redpine(KEY)
    assert c.get_results("q-1").query_id == "q-1"
    assert c.quota().daily_remaining == 9
    assert c.collections().collections[0].name == "corpus"


@respx.mock
def test_base_url_env_is_used(monkeypatch):
    monkeypatch.setenv("REDPINE_BASE_URL", "http://local.test")
    route = respx.get("http://local.test/api/v1/search/quota").mock(
        return_value=httpx.Response(
            200,
            json={
                "dailyLimit": 1,
                "dailyUsed": 0,
                "dailyRemaining": 1,
                "monthlyLimit": 1,
                "monthlyUsed": 0,
                "monthlyRemaining": 1,
            },
        )
    )
    Redpine(KEY).quota()
    assert route.called


# --- errors + retries -------------------------------------------------------


def _err(status, code):
    return httpx.Response(status, json={"error": {"code": code, "message": "m", "requestId": "r"}})


@respx.mock
def test_403_maps_to_access_denied():
    respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(return_value=_err(403, "FORBIDDEN"))
    with pytest.raises(AccessDenied) as ei:
        Redpine(KEY).search("q", collection="c")
    assert ei.value.code == "FORBIDDEN" and ei.value.request_id == "r"


@respx.mock
def test_429_retries_then_succeeds(monkeypatch):
    sleeps = []
    monkeypatch.setattr("redpine.client.time.sleep", lambda s: sleeps.append(s))
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query")
    route.side_effect = [
        httpx.Response(
            429,
            headers={"Retry-After": "2"},
            json={"error": {"code": "RATE_LIMITED", "message": "m"}},
        ),
        httpx.Response(200, json=SEARCH_OK),
    ]
    r = Redpine(KEY, max_retries=2).search("q", collection="c")
    assert r.query_id == "q-1"
    assert route.call_count == 2
    assert sleeps == [2.0]


@respx.mock
def test_429_exhausts_and_raises(monkeypatch):
    monkeypatch.setattr("redpine.client.time.sleep", lambda s: None)
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(
        return_value=_err(429, "RATE_LIMITED")
    )
    with pytest.raises(QuotaExceeded):
        Redpine(KEY, max_retries=2).search("q", collection="c")
    assert route.call_count == 3


@respx.mock
def test_4xx_does_not_retry(monkeypatch):
    monkeypatch.setattr("redpine.client.time.sleep", lambda s: None)
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(
        return_value=_err(401, "UNAUTHORIZED")
    )
    with pytest.raises(AuthError):
        Redpine(KEY, max_retries=3).search("q", collection="c")
    assert route.call_count == 1


def test_search_requires_exactly_one_target():
    c = Redpine(KEY)
    with pytest.raises(ValueError):
        c.search("q")
    with pytest.raises(ValueError):
        c.search("q", collection="a", collections=["b"])
    with pytest.raises(ValueError):
        c.search("q", collections=[])


@respx.mock
def test_search_empty_collections_with_collection_is_valid():
    route = respx.post(f"{DEFAULT_BASE_URL}/api/v1/search/query").mock(
        return_value=httpx.Response(200, json=SEARCH_OK)
    )
    c = Redpine(KEY)
    c.search("q", collection="a", collections=[])
    body = json.loads(route.calls.last.request.content)
    assert body["collection"] == "a"
    assert "collections" not in body
