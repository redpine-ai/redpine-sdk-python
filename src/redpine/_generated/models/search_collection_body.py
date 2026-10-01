from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_collection_body_filters_type_0 import SearchCollectionBodyFiltersType0


T = TypeVar("T", bound="SearchCollectionBody")


@_attrs_define
class SearchCollectionBody:
    """Same knobs as SearchRequest minus `collection`/`collections` — the target collection is the path segment, so a
    `collection` key in the body is rejected.

        Attributes:
            query (str): Natural language or keyword search query.
            filters (None | SearchCollectionBodyFiltersType0 | Unset): Optional metadata filter. Two accepted forms.

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
            image_max_height (int | Unset): Maximum image height in pixels Default: 600.
            image_max_width (int | Unset): Maximum image width in pixels Default: 800.
            image_quality (int | Unset): JPEG quality for fetched images Default: 75.
            include_figures (bool | Unset): Fetch and include figure images as base64 in metadata (adds latency).
                includeImages is accepted as a deprecated alias. Default: False.
            include_metadata (bool | Unset): Whether to include metadata in results Default: True.
            limit (int | Unset): Maximum results to return (default 10, max 30) Default: 10.
    """

    query: str
    filters: None | SearchCollectionBodyFiltersType0 | Unset = UNSET
    image_max_height: int | Unset = 600
    image_max_width: int | Unset = 800
    image_quality: int | Unset = 75
    include_figures: bool | Unset = False
    include_metadata: bool | Unset = True
    limit: int | Unset = 10

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_collection_body_filters_type_0 import SearchCollectionBodyFiltersType0

        query = self.query

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, SearchCollectionBodyFiltersType0):
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

        field_dict.update(
            {
                "query": query,
            }
        )
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
        from ..models.search_collection_body_filters_type_0 import SearchCollectionBodyFiltersType0

        d = dict(src_dict)
        query = d.pop("query")

        def _parse_filters(data: object) -> None | SearchCollectionBodyFiltersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = SearchCollectionBodyFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchCollectionBodyFiltersType0 | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        image_max_height = d.pop("imageMaxHeight", UNSET)

        image_max_width = d.pop("imageMaxWidth", UNSET)

        image_quality = d.pop("imageQuality", UNSET)

        include_figures = d.pop("includeFigures", UNSET)

        include_metadata = d.pop("includeMetadata", UNSET)

        limit = d.pop("limit", UNSET)

        search_collection_body = cls(
            query=query,
            filters=filters,
            image_max_height=image_max_height,
            image_max_width=image_max_width,
            image_quality=image_quality,
            include_figures=include_figures,
            include_metadata=include_metadata,
            limit=limit,
        )

        return search_collection_body
