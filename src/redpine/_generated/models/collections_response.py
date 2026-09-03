from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.collections_response_collections_item import CollectionsResponseCollectionsItem


T = TypeVar("T", bound="CollectionsResponse")


@_attrs_define
class CollectionsResponse:
    """
    Attributes:
        collections (list[CollectionsResponseCollectionsItem]): List of accessible collections.
        count (int): Total number of accessible collections.
    """

    collections: list[CollectionsResponseCollectionsItem]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collections = []
        for collections_item_data in self.collections:
            collections_item = collections_item_data.to_dict()
            collections.append(collections_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collections": collections,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.collections_response_collections_item import (
            CollectionsResponseCollectionsItem,
        )

        d = dict(src_dict)
        collections = []
        _collections = d.pop("collections")
        for collections_item_data in _collections:
            collections_item = CollectionsResponseCollectionsItem.from_dict(collections_item_data)

            collections.append(collections_item)

        count = d.pop("count")

        collections_response = cls(
            collections=collections,
            count=count,
        )

        collections_response.additional_properties = d
        return collections_response

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
