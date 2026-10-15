from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.discovery_collection_item_price_range_type_0_per import (
    DiscoveryCollectionItemPriceRangeType0Per,
)

T = TypeVar("T", bound="DiscoveryCollectionItemPriceRangeType0")


@_attrs_define
class DiscoveryCollectionItemPriceRangeType0:
    """Min/max member price when a meta-collection's members differ

    Attributes:
        max_ (str): Highest member price per 1000 tokens
        min_ (str): Lowest member price per 1000 tokens
        per (DiscoveryCollectionItemPriceRangeType0Per):
    """

    max_: str
    min_: str
    per: DiscoveryCollectionItemPriceRangeType0Per
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        min_ = self.min_

        per = self.per.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max": max_,
                "min": min_,
                "per": per,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        max_ = d.pop("max")

        min_ = d.pop("min")

        per = DiscoveryCollectionItemPriceRangeType0Per(d.pop("per"))

        discovery_collection_item_price_range_type_0 = cls(
            max_=max_,
            min_=min_,
            per=per,
        )

        discovery_collection_item_price_range_type_0.additional_properties = d
        return discovery_collection_item_price_range_type_0

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
