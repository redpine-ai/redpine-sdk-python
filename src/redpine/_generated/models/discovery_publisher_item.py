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
        kind (DiscoveryPublisherItemKind):  Default: DiscoveryPublisherItemKind.PUBLISHER.
        name (str): Publisher name as stored in the corpus
        collections (list[str] | Unset): Collections (display names) it appears in
    """

    name: str
    kind: DiscoveryPublisherItemKind = DiscoveryPublisherItemKind.PUBLISHER
    collections: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        collections: list[str] | Unset = UNSET
        if not isinstance(self.collections, Unset):
            collections = self.collections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "name": name,
            }
        )
        if collections is not UNSET:
            field_dict["collections"] = collections

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = DiscoveryPublisherItemKind(d.pop("kind"))

        name = d.pop("name")

        collections = cast(list[str], d.pop("collections", UNSET))

        discovery_publisher_item = cls(
            kind=kind,
            name=name,
            collections=collections,
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
