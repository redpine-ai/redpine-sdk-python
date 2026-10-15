from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.discovery_collection_item_kind import DiscoveryCollectionItemKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_collection_item_price_range_type_0 import (
        DiscoveryCollectionItemPriceRangeType0,
    )


T = TypeVar("T", bound="DiscoveryCollectionItem")


@_attrs_define
class DiscoveryCollectionItem:
    """
    Attributes:
        collection_kind (str): physical, publisher, journal, curated or meta
        display_name (str): Display name
        name (str): Collection name to pass to search
        revenue_model (str): licensed or open_access
        description (None | str | Unset): Collection description
        kind (DiscoveryCollectionItemKind | Unset):  Default: DiscoveryCollectionItemKind.COLLECTION.
        members (list[str] | None | Unset): Member display names (metas only)
        price_per_1000 (None | str | Unset): Your organisation's price per 1000 tokens, when a single price applies
        price_range (DiscoveryCollectionItemPriceRangeType0 | None | Unset): Min/max member price when a meta-
            collection's members differ
    """

    collection_kind: str
    display_name: str
    name: str
    revenue_model: str
    description: None | str | Unset = UNSET
    kind: DiscoveryCollectionItemKind | Unset = DiscoveryCollectionItemKind.COLLECTION
    members: list[str] | None | Unset = UNSET
    price_per_1000: None | str | Unset = UNSET
    price_range: DiscoveryCollectionItemPriceRangeType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discovery_collection_item_price_range_type_0 import (
            DiscoveryCollectionItemPriceRangeType0,
        )

        collection_kind = self.collection_kind

        display_name = self.display_name

        name = self.name

        revenue_model = self.revenue_model

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        members: list[str] | None | Unset
        if isinstance(self.members, Unset):
            members = UNSET
        elif isinstance(self.members, list):
            members = self.members

        else:
            members = self.members

        price_per_1000: None | str | Unset
        if isinstance(self.price_per_1000, Unset):
            price_per_1000 = UNSET
        else:
            price_per_1000 = self.price_per_1000

        price_range: dict[str, Any] | None | Unset
        if isinstance(self.price_range, Unset):
            price_range = UNSET
        elif isinstance(self.price_range, DiscoveryCollectionItemPriceRangeType0):
            price_range = self.price_range.to_dict()
        else:
            price_range = self.price_range

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collectionKind": collection_kind,
                "displayName": display_name,
                "name": name,
                "revenueModel": revenue_model,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if kind is not UNSET:
            field_dict["kind"] = kind
        if members is not UNSET:
            field_dict["members"] = members
        if price_per_1000 is not UNSET:
            field_dict["pricePer1000"] = price_per_1000
        if price_range is not UNSET:
            field_dict["priceRange"] = price_range

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.discovery_collection_item_price_range_type_0 import (
            DiscoveryCollectionItemPriceRangeType0,
        )

        d = dict(src_dict)
        collection_kind = d.pop("collectionKind")

        display_name = d.pop("displayName")

        name = d.pop("name")

        revenue_model = d.pop("revenueModel")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _kind = d.pop("kind", UNSET)
        kind: DiscoveryCollectionItemKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = DiscoveryCollectionItemKind(_kind)

        def _parse_members(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                members_type_0 = cast(list[str], data)

                return members_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        members = _parse_members(d.pop("members", UNSET))

        def _parse_price_per_1000(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_per_1000 = _parse_price_per_1000(d.pop("pricePer1000", UNSET))

        def _parse_price_range(
            data: object,
        ) -> DiscoveryCollectionItemPriceRangeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                price_range_type_0 = DiscoveryCollectionItemPriceRangeType0.from_dict(data)

                return price_range_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiscoveryCollectionItemPriceRangeType0 | None | Unset, data)

        price_range = _parse_price_range(d.pop("priceRange", UNSET))

        discovery_collection_item = cls(
            collection_kind=collection_kind,
            display_name=display_name,
            name=name,
            revenue_model=revenue_model,
            description=description,
            kind=kind,
            members=members,
            price_per_1000=price_per_1000,
            price_range=price_range,
        )

        discovery_collection_item.additional_properties = d
        return discovery_collection_item

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
