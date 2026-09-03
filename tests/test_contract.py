"""Replay spec/fixtures/*.json against the sync client. Shared with TS and Go."""

import json
from pathlib import Path

import httpx
import pytest
import respx

import redpine
from redpine import Redpine
from redpine.client import DEFAULT_BASE_URL


def _fixtures_dir() -> Path:
    here = Path(__file__).resolve()
    # monorepo: python/tests -> ../../spec; public repo: tests -> ../spec
    for candidate in (here.parents[2] / "spec" / "fixtures", here.parents[1] / "spec" / "fixtures"):
        if candidate.is_dir():
            return candidate
    raise FileNotFoundError("spec/fixtures not found next to the package")


FIXTURES = sorted(_fixtures_dir().glob("*.json"))
assert FIXTURES, "spec/fixtures is empty"
KEY = "sk_test_fake_contract"


def _field(obj, camel_name: str):
    # generated attrs models expose snake_case attributes
    snake = "".join("_" + c.lower() if c.isupper() else c for c in camel_name)
    return getattr(obj, snake)


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    for v in ("REDPINE_API_KEY", "CONNECT_API_KEY", "REDPINE_BASE_URL"):
        monkeypatch.delenv(v, raising=False)
    monkeypatch.setattr("redpine.client.time.sleep", lambda s: None)


@pytest.mark.parametrize("path", FIXTURES, ids=[p.stem for p in FIXTURES])
@respx.mock
def test_fixture(path: Path):
    fx = json.loads(path.read_text())
    req, resp, exp = fx["request"], fx["response"], fx["expect"]
    route = respx.route(method=req["method"], url=f"{DEFAULT_BASE_URL}{req['path']}").mock(
        return_value=httpx.Response(resp["status"], headers=resp["headers"], json=resp["body"])
    )

    client = Redpine(KEY, max_retries=0)
    fn = getattr(client, fx["op"])
    if exp["error"]:
        with pytest.raises(getattr(redpine, exp["error"])) as ei:
            fn(**fx["args"])
        if exp.get("retry_after") is not None:
            assert ei.value.retry_after == exp["retry_after"]
    else:
        result = fn(**fx["args"])
        assert _field(result, exp["field"]) == exp["value"]

    sent = route.calls.last.request
    assert sent.method == req["method"]
    body = json.loads(sent.content) if sent.content else None
    assert body == req["body"]
