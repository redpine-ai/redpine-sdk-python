from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assisted_search_result_metadata_type_0 import AssistedSearchResultMetadataType0
    from ..models.relevance_info import RelevanceInfo


T = TypeVar("T", bound="AssistedSearchResult")


@_attrs_define
class AssistedSearchResult:
    """
    Attributes:
        id (str): Chunk/point ID
        relevance (RelevanceInfo): Why a result was judged relevant.
        text (str): Chunk text content
        collection (None | str | Unset): Origin collection of this result. Populated only for requests made with the
            'collections' (multi-collection) form.
        doi_url (None | str | Unset): Resolvable DOI link (https://doi.org/{doi})
        metadata (AssistedSearchResultMetadataType0 | None | Unset): Document metadata (title, authors, journal, etc.).
            Null when includeMetadata is false.
        section (None | str | Unset): Comma-joined source section(s) of the article, from the normalized vocabulary
            (abstract, introduction, background, methods, results, discussion, conclusion, case, supplementary, other)
    """

    id: str
    relevance: RelevanceInfo
    text: str
    collection: None | str | Unset = UNSET
    doi_url: None | str | Unset = UNSET
    metadata: AssistedSearchResultMetadataType0 | None | Unset = UNSET
    section: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.assisted_search_result_metadata_type_0 import (
            AssistedSearchResultMetadataType0,
        )

        id = self.id

        relevance = self.relevance.to_dict()

        text = self.text

        collection: None | str | Unset
        if isinstance(self.collection, Unset):
            collection = UNSET
        else:
            collection = self.collection

        doi_url: None | str | Unset
        if isinstance(self.doi_url, Unset):
            doi_url = UNSET
        else:
            doi_url = self.doi_url

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AssistedSearchResultMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        section: None | str | Unset
        if isinstance(self.section, Unset):
            section = UNSET
        else:
            section = self.section

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "relevance": relevance,
                "text": text,
            }
        )
        if collection is not UNSET:
            field_dict["collection"] = collection
        if doi_url is not UNSET:
            field_dict["doiUrl"] = doi_url
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if section is not UNSET:
            field_dict["section"] = section

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assisted_search_result_metadata_type_0 import (
            AssistedSearchResultMetadataType0,
        )
        from ..models.relevance_info import RelevanceInfo

        d = dict(src_dict)
        id = d.pop("id")

        relevance = RelevanceInfo.from_dict(d.pop("relevance"))

        text = d.pop("text")

        def _parse_collection(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection = _parse_collection(d.pop("collection", UNSET))

        def _parse_doi_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        doi_url = _parse_doi_url(d.pop("doiUrl", UNSET))

        def _parse_metadata(data: object) -> AssistedSearchResultMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AssistedSearchResultMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssistedSearchResultMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_section(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        section = _parse_section(d.pop("section", UNSET))

        assisted_search_result = cls(
            id=id,
            relevance=relevance,
            text=text,
            collection=collection,
            doi_url=doi_url,
            metadata=metadata,
            section=section,
        )

        assisted_search_result.additional_properties = d
        return assisted_search_result

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
