import pytest

from redpine._retry import RETRYABLE_STATUSES, backoff_seconds, should_retry


def test_retryable_set():
    assert RETRYABLE_STATUSES == frozenset({429, 503})


@pytest.mark.parametrize("status", [200, 400, 401, 403, 404, 422, 500, 502])
def test_non_retryable_statuses_never_retry(status):
    assert should_retry(status, attempt=0, max_retries=5) is False


def test_retries_until_budget_spent():
    assert should_retry(429, attempt=0, max_retries=2) is True
    assert should_retry(429, attempt=1, max_retries=2) is True
    assert should_retry(429, attempt=2, max_retries=2) is False
    assert should_retry(503, attempt=0, max_retries=0) is False


def test_retry_after_wins():
    assert backoff_seconds(0, retry_after=7.0) == 7.0
    assert backoff_seconds(3, retry_after=1.5) == 1.5


def test_exponential_with_full_jitter():
    # rand=1.0 gives the ceiling, rand=0.0 gives zero
    assert backoff_seconds(0, None, rand=lambda: 1.0) == 0.5
    assert backoff_seconds(1, None, rand=lambda: 1.0) == 1.0
    assert backoff_seconds(2, None, rand=lambda: 1.0) == 2.0
    assert backoff_seconds(2, None, rand=lambda: 0.0) == 0.0


def test_cap():
    assert backoff_seconds(20, None, rand=lambda: 1.0) == 30.0
