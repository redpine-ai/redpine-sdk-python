from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.discovery_callout_kind import DiscoveryCalloutKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryCallout")


@_attrs_define
class DiscoveryCallout:
    """
    Attributes:
        message (str): The notice, verbatim
        kind (DiscoveryCalloutKind | Unset):  Default: DiscoveryCalloutKind.ADD_PAYMENT_METHOD.
    """

    message: str
    kind: DiscoveryCalloutKind | Unset = DiscoveryCalloutKind.ADD_PAYMENT_METHOD
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        message = d.pop("message")

        _kind = d.pop("kind", UNSET)
        kind: DiscoveryCalloutKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = DiscoveryCalloutKind(_kind)

        discovery_callout = cls(
            message=message,
            kind=kind,
        )

        discovery_callout.additional_properties = d
        return discovery_callout

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
