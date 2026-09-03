"""Retry policy: 429 and 503 only, exponential backoff with full jitter, Retry-After wins."""

from __future__ import annotations

import random
from collections.abc import Callable

RETRYABLE_STATUSES = frozenset({429, 503})


def should_retry(status: int, attempt: int, max_retries: int) -> bool:
    """`attempt` is zero-based: the number of retries already made."""
    return status in RETRYABLE_STATUSES and attempt < max_retries


def backoff_seconds(
    attempt: int,
    retry_after: float | None,
    *,
    base: float = 0.5,
    factor: float = 2.0,
    cap: float = 30.0,
    rand: Callable[[], float] = random.random,
) -> float:
    if retry_after is not None:
        return retry_after
    ceiling = min(cap, base * (factor**attempt))
    return ceiling * rand()
