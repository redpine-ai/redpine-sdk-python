from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_request_filters_type_0 import SearchRequestFiltersType0


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """Provide exactly one of `collection` (single) or `collections` (multi-collection search).

    Attributes:
        query (str): Natural language or keyword search query.
        collection (None | str | Unset): Name of the collection to search. Mutually exclusive with `collections`.
        collections (list[str] | None | Unset): Collections to search together (max 5, unique). Each collection is
            searched with its own access entitlements and the results are merged into one relevance-ranked list; each result
            carries its origin `collection`. Mutually exclusive with `collection`.
        filters (None | SearchRequestFiltersType0 | Unset): Optional metadata filter. Two accepted forms.

            Flat (top-level keys are ANDed): `{"journal": "Nature", "publication_date": {"gte": "2020-01-01"}}`.

            Structured DSL (for OR / nesting): `{"and": [{"field": "journal", "eq": "Nature"}]}`. Operators: `eq`, `ne`,
            `in`, `not_in`, `gt`, `gte`, `lt`, `lte`, `between`. Combinators: `and`, `or`, `not`.

            Exclusion uses `ne` / `not_in` / `not` — there is no separate syntax: `{"and": [{"field": "issn", "not_in":
            ["1234-5678"]}]}`.

            Indexed on every collection (any other field is matched by scanning and returns a `filterWarnings` entry):
            `article_type`, `chapter_authors`, `chapter_number`, `chapter_title`, `doc_id`, `doi`, `isbn`, `issn`,
            `journal`, `keywords`, `license`, `open_access`, `publication_date`, `publisher`, `section`.

            Indexed on the editorial collections only (People Inc): `last_updated_date`, `medical_board_approved`, `topic`,
            `url`.

            `issn` accepts hyphenated or bare, upper- or lower-case X (`"1664-302X"`, `"1664302x"`). `doi` is matched case-
            insensitively and an optional `https://doi.org/` or `doi:` prefix is accepted.

            `journal_metric.2yr_mean_citedness`, `journal_metric.h_index` and `journal_metric.i10_index` accept range
            operators only and are resolved server-side into the matching ISSNs; see `journalMetricExpansions` in the
            response.
        image_max_height (int | Unset): Maximum image height in pixels Default: 600.
        image_max_width (int | Unset): Maximum image width in pixels Default: 800.
        image_quality (int | Unset): JPEG quality for fetched images Default: 75.
        include_figures (bool | Unset): Fetch and include figure images as base64 in metadata (adds latency).
            includeImages is accepted as a deprecated alias. Default: False.
        include_metadata (bool | Unset): Whether to include metadata in results Default: True.
        limit (int | Unset): Maximum results to return (default 10, max 30) Default: 10.
    """

    query: str
    collection: None | str | Unset = UNSET
    collections: list[str] | None | Unset = UNSET
    filters: None | SearchRequestFiltersType0 | Unset = UNSET
    image_max_height: int | Unset = 600
    image_max_width: int | Unset = 800
    image_quality: int | Unset = 75
    include_figures: bool | Unset = False
    include_metadata: bool | Unset = True
    limit: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_request_filters_type_0 import SearchRequestFiltersType0

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
        elif isinstance(self.filters, SearchRequestFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

        image_max_height = self.image_max_height

        image_max_width = self.image_max_width

        image_quality = self.image_quality

        include_figures = self.include_figures

        include_metadata = self.include_metadata

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
        if image_max_height is not UNSET:
            field_dict["imageMaxHeight"] = image_max_height
        if image_max_width is not UNSET:
            field_dict["imageMaxWidth"] = image_max_width
        if image_quality is not UNSET:
            field_dict["imageQuality"] = image_quality
        if include_figures is not UNSET:
            field_dict["includeFigures"] = include_figures
        if include_metadata is not UNSET:
            field_dict["includeMetadata"] = include_metadata
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.search_request_filters_type_0 import SearchRequestFiltersType0

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

        def _parse_filters(data: object) -> None | SearchRequestFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = SearchRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchRequestFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        image_max_height = d.pop("imageMaxHeight", UNSET)

        image_max_width = d.pop("imageMaxWidth", UNSET)

        image_quality = d.pop("imageQuality", UNSET)

        include_figures = d.pop("includeFigures", UNSET)

        include_metadata = d.pop("includeMetadata", UNSET)

        limit = d.pop("limit", UNSET)

        search_request = cls(
            query=query,
            collection=collection,
            collections=collections,
            filters=filters,
            image_max_height=image_max_height,
            image_max_width=image_max_width,
            image_quality=image_quality,
            include_figures=include_figures,
            include_metadata=include_metadata,
            limit=limit,
        )

        search_request.additional_properties = d
        return search_request

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
