from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assisted_search_request_filters_type_0 import AssistedSearchRequestFiltersType0


T = TypeVar("T", bound="AssistedSearchRequest")


@_attrs_define
class AssistedSearchRequest:
    """
    Attributes:
        query (str): Search query text
        allow_clarification (bool | Unset): If true, the endpoint may return a clarifying question instead of results
            when the query is too underspecified. Set false if your client cannot do a follow-up turn. Default: True.
        collection (None | str | Unset): Collection to search. Provide either this or `collections`, not both.
        collections (list[str] | None | Unset): Collections to search together (max 5). Results are merged into one
            relevance-ranked list and each result is labeled with its origin collection. Provide either this or
            'collection', not both.
        filters (AssistedSearchRequestFiltersType0 | None | Unset): Same filter forms as `/api/v1/search/query`; applied
            to every internal search.
        image_max_height (int | Unset): Maximum image height in pixels Default: 600.
        image_max_width (int | Unset): Maximum image width in pixels Default: 800.
        image_quality (int | Unset): JPEG quality for fetched images Default: 75.
        include_figures (bool | Unset): Fetch and attach figure images (base64, in metadata.figures[].image_data) for
            the delivered results only. Adds latency; requires `includeMetadata`. `includeImages` is accepted as a
            deprecated alias. Default: False.
        include_metadata (bool | Unset): Whether to include metadata in results Default: True.
        limit (int | Unset): Maximum verified results to return. Default: 10.
    """

    query: str
    allow_clarification: bool | Unset = True
    collection: None | str | Unset = UNSET
    collections: list[str] | None | Unset = UNSET
    filters: AssistedSearchRequestFiltersType0 | None | Unset = UNSET
    image_max_height: int | Unset = 600
    image_max_width: int | Unset = 800
    image_quality: int | Unset = 75
    include_figures: bool | Unset = False
    include_metadata: bool | Unset = True
    limit: int | Unset = 10
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assisted_search_request_filters_type_0 import (
            AssistedSearchRequestFiltersType0,
        )

        query = self.query

        allow_clarification = self.allow_clarification

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
        elif isinstance(self.filters, AssistedSearchRequestFiltersType0):
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
        if allow_clarification is not UNSET:
            field_dict["allowClarification"] = allow_clarification
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
        from ..models.assisted_search_request_filters_type_0 import (
            AssistedSearchRequestFiltersType0,
        )

        d = dict(src_dict)
        query = d.pop("query")

        allow_clarification = d.pop("allowClarification", UNSET)

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

        def _parse_filters(data: object) -> AssistedSearchRequestFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = AssistedSearchRequestFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssistedSearchRequestFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        image_max_height = d.pop("imageMaxHeight", UNSET)

        image_max_width = d.pop("imageMaxWidth", UNSET)

        image_quality = d.pop("imageQuality", UNSET)

        include_figures = d.pop("includeFigures", UNSET)

        include_metadata = d.pop("includeMetadata", UNSET)

        limit = d.pop("limit", UNSET)

        assisted_search_request = cls(
            query=query,
            allow_clarification=allow_clarification,
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

        assisted_search_request.additional_properties = d
        return assisted_search_request

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
