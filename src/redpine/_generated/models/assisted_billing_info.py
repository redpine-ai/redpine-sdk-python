from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AssistedBillingInfo")


@_attrs_define
class AssistedBillingInfo:
    """What was actually charged — only delivered, verified results are billed.

    Attributes:
        charged_results (int): Number of results billed
        tokens_charged (int): Tokens billed (0 for clarification/no-result)
    """

    charged_results: int
    tokens_charged: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        charged_results = self.charged_results

        tokens_charged = self.tokens_charged

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "chargedResults": charged_results,
                "tokensCharged": tokens_charged,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        charged_results = d.pop("chargedResults")

        tokens_charged = d.pop("tokensCharged")

        assisted_billing_info = cls(
            charged_results=charged_results,
            tokens_charged=tokens_charged,
        )

        assisted_billing_info.additional_properties = d
        return assisted_billing_info

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
