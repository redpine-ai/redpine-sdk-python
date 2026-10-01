from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnlockRequest")


@_attrs_define
class UnlockRequest:
    """
    Attributes:
        query_id (str): The `queryId` from a previous POST /search/preview response.
        image_max_height (int | Unset): Maximum image height in pixels Default: 600.
        image_max_width (int | Unset): Maximum image width in pixels Default: 800.
        image_quality (int | Unset): JPEG quality for fetched images Default: 75.
        include_figures (bool | Unset): Fetch figure images, returned as base64 in each result's metadata. Candidates
            are every result unlocked under this queryId, this call's and earlier calls' alike, but at most 50 images are
            fetched per call: the ids in resultIds — or, when it is omitted, the results this call unlocked — get that
            budget first, and figures past it come back as captions with no image_data. Ask again for the ids you still
            want; re-sending ids already unlocked charges nothing. Free — figures are not priced into the token cost, so
            this changes latency and response size, never the charge. Off by default: use the preview's figureCount to
            decide. includeImages is a deprecated alias. Default: False.
        result_ids (list[str] | None | Unset): Result ids to unlock. Omit (or pass `null`) to unlock every result from
            the preview. Re-sending an id that is already unlocked costs nothing — only the delta is charged.
    """

    query_id: str
    image_max_height: int | Unset = 600
    image_max_width: int | Unset = 800
    image_quality: int | Unset = 75
    include_figures: bool | Unset = False
    result_ids: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query_id = self.query_id

        image_max_height = self.image_max_height

        image_max_width = self.image_max_width

        image_quality = self.image_quality

        include_figures = self.include_figures

        result_ids: list[str] | None | Unset
        if isinstance(self.result_ids, Unset):
            result_ids = UNSET
        elif isinstance(self.result_ids, list):
            result_ids = self.result_ids

        else:
            result_ids = self.result_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queryId": query_id,
            }
        )
        if image_max_height is not UNSET:
            field_dict["imageMaxHeight"] = image_max_height
        if image_max_width is not UNSET:
            field_dict["imageMaxWidth"] = image_max_width
        if image_quality is not UNSET:
            field_dict["imageQuality"] = image_quality
        if include_figures is not UNSET:
            field_dict["includeFigures"] = include_figures
        if result_ids is not UNSET:
            field_dict["resultIds"] = result_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        query_id = d.pop("queryId")

        image_max_height = d.pop("imageMaxHeight", UNSET)

        image_max_width = d.pop("imageMaxWidth", UNSET)

        image_quality = d.pop("imageQuality", UNSET)

        include_figures = d.pop("includeFigures", UNSET)

        def _parse_result_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_ids_type_0 = cast(list[str], data)

                return result_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        result_ids = _parse_result_ids(d.pop("resultIds", UNSET))

        unlock_request = cls(
            query_id=query_id,
            image_max_height=image_max_height,
            image_max_width=image_max_width,
            image_quality=image_quality,
            include_figures=include_figures,
            result_ids=result_ids,
        )

        unlock_request.additional_properties = d
        return unlock_request

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
