from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.discovery_publisher_item_kind import DiscoveryPublisherItemKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryPublisherItem")


@_attrs_define
class DiscoveryPublisherItem:
    """
    Attributes:
        name (str): Publisher name as stored in the corpus
        collections (list[str] | Unset): Collections (display names) it appears in
        kind (DiscoveryPublisherItemKind | Unset):  Default: DiscoveryPublisherItemKind.PUBLISHER.
    """

    name: str
    collections: list[str] | Unset = UNSET
    kind: DiscoveryPublisherItemKind | Unset = DiscoveryPublisherItemKind.PUBLISHER
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        collections: list[str] | Unset = UNSET
        if not isinstance(self.collections, Unset):
            collections = self.collections

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if collections is not UNSET:
            field_dict["collections"] = collections
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        collections = cast(list[str], d.pop("collections", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: DiscoveryPublisherItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = DiscoveryPublisherItemKind(_kind)

        discovery_publisher_item = cls(
            name=name,
            collections=collections,
            kind=kind,
        )

        discovery_publisher_item.additional_properties = d
        return discovery_publisher_item

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
