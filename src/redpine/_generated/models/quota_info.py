from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="QuotaInfo")


@_attrs_define
class QuotaInfo:
    """
    Attributes:
        daily_limit (int): Max queries per day.
        daily_remaining (int): Queries remaining today.
        daily_used (int): Queries used today.
        monthly_limit (int): Max queries per month.
        monthly_remaining (int): Queries remaining this month.
        monthly_used (int): Queries used this month.
    """

    daily_limit: int
    daily_remaining: int
    daily_used: int
    monthly_limit: int
    monthly_remaining: int
    monthly_used: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_limit = self.daily_limit

        daily_remaining = self.daily_remaining

        daily_used = self.daily_used

        monthly_limit = self.monthly_limit

        monthly_remaining = self.monthly_remaining

        monthly_used = self.monthly_used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dailyLimit": daily_limit,
                "dailyRemaining": daily_remaining,
                "dailyUsed": daily_used,
                "monthlyLimit": monthly_limit,
                "monthlyRemaining": monthly_remaining,
                "monthlyUsed": monthly_used,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        daily_limit = d.pop("dailyLimit")

        daily_remaining = d.pop("dailyRemaining")

        daily_used = d.pop("dailyUsed")

        monthly_limit = d.pop("monthlyLimit")

        monthly_remaining = d.pop("monthlyRemaining")

        monthly_used = d.pop("monthlyUsed")

        quota_info = cls(
            daily_limit=daily_limit,
            daily_remaining=daily_remaining,
            daily_used=daily_used,
            monthly_limit=monthly_limit,
            monthly_remaining=monthly_remaining,
            monthly_used=monthly_used,
        )

        quota_info.additional_properties = d
        return quota_info

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
