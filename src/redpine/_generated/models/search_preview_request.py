from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_preview_request_filters_type_0 import SearchPreviewRequestFiltersType0


T = TypeVar("T", bound="SearchPreviewRequest")


@_attrs_define
class SearchPreviewRequest:
    """The result-selection half of SearchRequest. A preview quotes results rather than delivering them, so it takes no
    content-delivery options: figures are never fetched (they are not priced into the quote) and metadata is always
    returned. Provide exactly one of `collection` (single) or `collections` (multi).

        Attributes:
            query (str): Natural language or keyword search query.
            collection (None | str | Unset): Name of the collection to search. Mutually exclusive with `collections`.
            collections (list[str] | None | Unset): Collections to search together (max 5, unique). Each collection is
                searched with its own access entitlements and the results are merged into one relevance-ranked list; each result
                carries its origin `collection`. Mutually exclusive with `collection`.
            filters (None | SearchPreviewRequestFiltersType0 | Unset): Optional metadata filter. Two accepted forms.

                Flat (top-level keys are ANDed): `{"journal": "Nature", "publication_date": {"gte": "2020-01-01"}}`.

                Structured DSL (for OR / nesting): `{"and": [{"field": "journal", "eq": "Nature"}]}`. Operators: `eq`, `ne`,
                `in`, `not_in`, `gt`, `gte`, `lt`, `lte`, `between`. Combinators: `and`, `or`, `not`. One operator per
                condition, except range bounds (`gt`, `gte`, `lt`, `lte`) together; put other combinations in separate
                conditions under `and`.

                Mixing the flat and structured forms in one filter is rejected.

                Exclusion uses `ne` / `not_in` / `not` — there is no separate syntax: `{"and": [{"field": "issn", "not_in":
                ["1234-5679"]}]}`.

                Indexed on every collection (a field that is not a known result metadata field is rejected; a known field
                without an index, such as `pmid`, is matched by scanning and returns a `filterWarnings` entry, and is rejected
                on a collection that has no index for it): `article_type`, `chapter_authors`, `chapter_number`, `chapter_title`,
                `doi`, `isbn`, `issn`, `journal`, `keywords`, `open_access`, `publication_date`, `publisher`, `section`.

                Indexed on the editorial collections only: `last_updated_date`, `medical_board_approved`, `topic`, `url`.

                `open_access` is also answered for a collection that holds only open-access content and carries no such field:
                `true` matches everything there, `false` (or the field under `or` / `not`) excludes that collection with a
                `filterWarnings` entry. `license` is returned in result metadata but is not filterable.

                `issn` accepts hyphenated or bare, upper- or lower-case X (`"1234-561X"`, `"1234561x"`). `doi` is matched case-
                insensitively and an optional `https://doi.org/` or `doi:` prefix is accepted.

                `journal_metric.2yr_mean_citedness`, `journal_metric.h_index` and `journal_metric.i10_index` accept range
                operators only and are resolved server-side into the matching ISSNs; see `journalMetricExpansions` in the
                response.
            limit (int | Unset): Maximum results to return (default 10, max 30) Default: 10.
    """

    query: str
    collection: None | str | Unset = UNSET
    collections: list[str] | None | Unset = UNSET
    filters: None | SearchPreviewRequestFiltersType0 | Unset = UNSET
    limit: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_preview_request_filters_type_0 import SearchPreviewRequestFiltersType0

        query = self.query

        collection: None | str | Unset
        if isinstance(self.collection, Unset):
            collection = UNSET
        else:
            collection = self.collection

        collections: list[str] | None | Unset
        if isinstance(self.collections, Unset):
            collections = UNSET
        elif isinstance(self.collections, list):
            collections = self.collections

        else:
            collections = self.collections

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, SearchPreviewRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if collection is not UNSET:
            field_dict["collection"] = collection
        if collections is not UNSET:
            field_dict["collections"] = collections
        if filters is not UNSET:
            field_dict["filters"] = filters
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_preview_request_filters_type_0 import SearchPreviewRequestFiltersType0

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_collection(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection = _parse_collection(d.pop("collection", UNSET))

        def _parse_collections(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collections_type_0 = cast(list[str], data)

                return collections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        collections = _parse_collections(d.pop("collections", UNSET))

        def _parse_filters(data: object) -> None | SearchPreviewRequestFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = SearchPreviewRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchPreviewRequestFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        limit = d.pop("limit", UNSET)

        search_preview_request = cls(
            query=query,
            collection=collection,
            collections=collections,
            filters=filters,
            limit=limit,
        )

        search_preview_request.additional_properties = d
        return search_preview_request

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
