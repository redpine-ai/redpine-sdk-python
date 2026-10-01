from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview_result_metadata_type_0 import PreviewResultMetadataType0


T = TypeVar("T", bound="PreviewResult")


@_attrs_define
class PreviewResult:
    """
    Attributes:
        figure_count (int): How many figures this result carries. Reported on locked rows too — the captions and images
            stay behind the paywall, but the count is what tells you whether unlocking with includeFigures is worth it. 0
            for text-only content. Default: 0.
        id (str): Chunk/point ID
        locked (bool): True when text is a teaser rather than the full chunk
        text (str): Full chunk text when `locked` is false. A short teaser snippet — never the full chunk — when
            `locked` is true.
        collection (None | str | Unset): Origin collection of this result — the name as requested, so a logical
            collection reports the logical name rather than the physical one it resolves to. Always populated.
        cost (None | str | Unset): Cost to unlock this one result.
        metadata (None | PreviewResultMetadataType0 | Unset): Document metadata (title, authors, journal, etc.). Always
            present on /search/preview and /search/unlock, which take no includeMetadata option. On /search/results it is
            null when the original search set includeMetadata to false. `figures` (captions, and `image_data` when images
            were requested) is present only on unlocked results — a locked result reports `figureCount` and nothing else
            about its figures.
        tokens (int | None | Unset): Billable tokens to unlock this result.
    """

    id: str
    locked: bool
    text: str
    figure_count: int = 0
    collection: None | str | Unset = UNSET
    cost: None | str | Unset = UNSET
    metadata: None | PreviewResultMetadataType0 | Unset = UNSET
    tokens: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.preview_result_metadata_type_0 import PreviewResultMetadataType0

        figure_count = self.figure_count

        id = self.id

        locked = self.locked

        text = self.text

        collection: None | str | Unset
        if isinstance(self.collection, Unset):
            collection = UNSET
        else:
            collection = self.collection

        cost: None | str | Unset
        if isinstance(self.cost, Unset):
            cost = UNSET
        else:
            cost = self.cost

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, PreviewResultMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        tokens: int | None | Unset
        if isinstance(self.tokens, Unset):
            tokens = UNSET
        else:
            tokens = self.tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "figureCount": figure_count,
                "id": id,
                "locked": locked,
                "text": text,
            }
        )
        if collection is not UNSET:
            field_dict["collection"] = collection
        if cost is not UNSET:
            field_dict["cost"] = cost
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tokens is not UNSET:
            field_dict["tokens"] = tokens

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.preview_result_metadata_type_0 import PreviewResultMetadataType0

        d = dict(src_dict)
        figure_count = d.pop("figureCount")

        id = d.pop("id")

        locked = d.pop("locked")

        text = d.pop("text")

        def _parse_collection(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection = _parse_collection(d.pop("collection", UNSET))

        def _parse_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost = _parse_cost(d.pop("cost", UNSET))

        def _parse_metadata(data: object) -> None | PreviewResultMetadataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = PreviewResultMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PreviewResultMetadataType0 | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_tokens(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        tokens = _parse_tokens(d.pop("tokens", UNSET))

        preview_result = cls(
            figure_count=figure_count,
            id=id,
            locked=locked,
            text=text,
            collection=collection,
            cost=cost,
            metadata=metadata,
            tokens=tokens,
        )

        preview_result.additional_properties = d
        return preview_result

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
