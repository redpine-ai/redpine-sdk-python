"""Live smoke against whatever REDPINE_BASE_URL points at. Skipped unless SMOKE=1."""

import os

import pytest

from redpine import Redpine

pytestmark = pytest.mark.skipif(os.environ.get("SMOKE") != "1", reason="set SMOKE=1 to run live")


def test_quota_collections_search():
    c = Redpine()  # key from REDPINE_API_KEY, base URL from REDPINE_BASE_URL
    q = c.quota()
    assert q.daily_limit >= 0
    cols = c.collections()
    assert cols.count == len(cols.collections)
    if cols.count:
        r = c.search("test", collection=cols.collections[0].name, limit=1)
        assert r.query_id
