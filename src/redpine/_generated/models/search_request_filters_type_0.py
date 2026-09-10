from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SearchRequestFiltersType0")


@_attrs_define
class SearchRequestFiltersType0:
    """Optional metadata filter. Two accepted forms.

    Flat (top-level keys are ANDed): `{"journal": "Nature", "publication_date": {"gte": "2020-01-01"}}`.

    Structured DSL (for OR / nesting): `{"and": [{"field": "journal", "eq": "Nature"}]}`. Operators: `eq`, `ne`, `in`,
    `not_in`, `gt`, `gte`, `lt`, `lte`, `between`. Combinators: `and`, `or`, `not`.

    Exclusion uses `ne` / `not_in` / `not` — there is no separate syntax: `{"and": [{"field": "issn", "not_in":
    ["1234-5679"]}]}`.

    Indexed on every collection (any other field is matched by scanning and returns a `filterWarnings` entry):
    `article_type`, `chapter_authors`, `chapter_number`, `chapter_title`, `doc_id`, `doi`, `isbn`, `issn`, `journal`,
    `keywords`, `open_access`, `publication_date`, `publisher`, `section`.

    Indexed on the editorial collections only: `last_updated_date`, `medical_board_approved`, `topic`, `url`.

    `open_access` is also answered for a collection that holds only open-access content and carries no such field:
    `true` matches everything there, `false` (or the field under `or` / `not`) excludes that collection with a
    `filterWarnings` entry. `license` is returned in result metadata but is not filterable.

    `issn` accepts hyphenated or bare, upper- or lower-case X (`"1234-561X"`, `"1234561x"`). `doi` is matched case-
    insensitively and an optional `https://doi.org/` or `doi:` prefix is accepted.

    `journal_metric.2yr_mean_citedness`, `journal_metric.h_index` and `journal_metric.i10_index` accept range operators
    only and are resolved server-side into the matching ISSNs; see `journalMetricExpansions` in the response.

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        search_request_filters_type_0 = cls()

        search_request_filters_type_0.additional_properties = d
        return search_request_filters_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
