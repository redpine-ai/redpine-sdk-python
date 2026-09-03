"""Typed builder over the structured filter DSL the search API accepts.

Wire grammar (connect-api/schemas/filter_definition.py):
  leaf        {"field": <name>, "<op>": <value>}
  combinator  {"and" | "or" | "not": [<nodes>]}      (always a list)
  ops         eq ne in not_in gt gte lt lte between   (between = [lo, hi])

    F("issn").eq("1664-302X") | F("issn").eq("1932-6203")
    F("journal_metric.2yr_mean_citedness").gte(5) & ~F("doi").eq("10.1/x")
"""

from __future__ import annotations

import copy
from typing import Any


class Filter:
    """An immutable filter node. Combine with &, |, ~; serialise with to_dict()."""

    __slots__ = ("_node",)

    def __init__(self, node: dict[str, Any]) -> None:
        self._node = node

    def to_dict(self) -> dict[str, Any]:
        return copy.deepcopy(self._node)

    def _combine(self, op: str, other: Filter) -> Filter:
        if not isinstance(other, Filter):
            return NotImplemented
        left = self._node[op] if set(self._node) == {op} else [self._node]
        right = other._node[op] if set(other._node) == {op} else [other._node]
        return Filter({op: [*left, *right]})

    def __and__(self, other: Filter) -> Filter:
        return self._combine("and", other)

    def __or__(self, other: Filter) -> Filter:
        return self._combine("or", other)

    def __invert__(self) -> Filter:
        return Filter({"not": [self._node]})

    def __repr__(self) -> str:
        return f"Filter({self._node!r})"


class Field:
    """`F("name")` — pick a field, then apply one operator."""

    __slots__ = ("_name",)

    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or not name:
            raise ValueError("field name must be a non-empty string")
        self._name = name

    def _leaf(self, op: str, value: Any) -> Filter:
        return Filter({"field": self._name, op: value})

    def eq(self, value: Any) -> Filter:
        return self._leaf("eq", value)

    def ne(self, value: Any) -> Filter:
        return self._leaf("ne", value)

    def in_(self, values: list[Any]) -> Filter:
        return self._leaf("in", list(values))

    def not_in(self, values: list[Any]) -> Filter:
        return self._leaf("not_in", list(values))

    def gt(self, value: Any) -> Filter:
        return self._leaf("gt", value)

    def gte(self, value: Any) -> Filter:
        return self._leaf("gte", value)

    def lt(self, value: Any) -> Filter:
        return self._leaf("lt", value)

    def lte(self, value: Any) -> Filter:
        return self._leaf("lte", value)

    def between(self, lo: Any, hi: Any) -> Filter:
        return self._leaf("between", [lo, hi])


F = Field


def to_filter_dict(value: Filter | dict[str, Any] | None) -> dict[str, Any] | None:
    """Accept a builder Filter, a raw dict (either DSL form), or None."""
    if value is None:
        return None
    if isinstance(value, Filter):
        return value.to_dict()
    if isinstance(value, dict):
        return value
    raise TypeError(f"filters must be a Filter, dict or None, got {type(value).__name__}")
