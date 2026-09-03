import pytest

from redpine.filters import F, to_filter_dict


def test_eq_leaf():
    assert F("issn").eq("1664-302X").to_dict() == {"field": "issn", "eq": "1664-302X"}


@pytest.mark.parametrize(
    "method,op,val",
    [
        ("ne", "ne", "x"),
        ("in_", "in", ["a", "b"]),
        ("not_in", "not_in", ["a"]),
        ("gt", "gt", 1),
        ("gte", "gte", 5),
        ("lt", "lt", 2),
        ("lte", "lte", 3),
    ],
)
def test_each_operator(method, op, val):
    assert getattr(F("f"), method)(val).to_dict() == {"field": "f", op: val}


def test_between():
    assert F("year").between(2020, 2024).to_dict() == {"field": "year", "between": [2020, 2024]}


def test_or_combinator():
    f = F("issn").eq("a") | F("issn").eq("b")
    assert f.to_dict() == {"or": [{"field": "issn", "eq": "a"}, {"field": "issn", "eq": "b"}]}


def test_and_combinator():
    f = F("journal").eq("Nature") & F("year").gte(2020)
    assert f.to_dict() == {
        "and": [{"field": "journal", "eq": "Nature"}, {"field": "year", "gte": 2020}]
    }


def test_not_wraps_in_list():
    f = ~F("doi").eq("10.1/x")
    assert f.to_dict() == {"not": [{"field": "doi", "eq": "10.1/x"}]}


def test_chained_same_combinator_flattens():
    f = F("a").eq(1) & F("b").eq(2) & F("c").eq(3)
    assert f.to_dict() == {
        "and": [
            {"field": "a", "eq": 1},
            {"field": "b", "eq": 2},
            {"field": "c", "eq": 3},
        ]
    }


def test_mixed_nests():
    f = (F("a").eq(1) | F("b").eq(2)) & ~F("c").eq(3)
    assert f.to_dict() == {
        "and": [
            {"or": [{"field": "a", "eq": 1}, {"field": "b", "eq": 2}]},
            {"not": [{"field": "c", "eq": 3}]},
        ]
    }


def test_to_filter_dict_passthrough_and_none():
    raw = {"journal": "Nature"}
    assert to_filter_dict(raw) is raw
    assert to_filter_dict(None) is None
    assert to_filter_dict(F("x").eq(1)) == {"field": "x", "eq": 1}


def test_to_filter_dict_rejects_other_types():
    with pytest.raises(TypeError):
        to_filter_dict("issn=1")  # type: ignore[arg-type]


def test_to_dict_returns_fresh_copy():
    f = F("x").eq(1)
    d = f.to_dict()
    d["eq"] = 2
    assert f.to_dict() == {"field": "x", "eq": 1}
