from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="JournalMetricExpansion")


@_attrs_define
class JournalMetricExpansion:
    """
    Attributes:
        condition (str): Threshold applied, e.g. `gte 5.0`.
        field (str): Metric field expanded, e.g. `journal_metric.2yr_mean_citedness`.
        issn_count (int): ISSNs pushed down (a journal usually has both a print and an electronic ISSN).
        matched_journals (int): Distinct journals matching the threshold.
        sample_issns (list[str] | Unset): First few ISSNs, for inspection.
    """

    condition: str
    field: str
    issn_count: int
    matched_journals: int
    sample_issns: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition = self.condition

        field = self.field

        issn_count = self.issn_count

        matched_journals = self.matched_journals

        sample_issns: list[str] | Unset = UNSET
        if not isinstance(self.sample_issns, Unset):
            sample_issns = self.sample_issns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition": condition,
                "field": field,
                "issnCount": issn_count,
                "matchedJournals": matched_journals,
            }
        )
        if sample_issns is not UNSET:
            field_dict["sampleIssns"] = sample_issns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        condition = d.pop("condition")

        field = d.pop("field")

        issn_count = d.pop("issnCount")

        matched_journals = d.pop("matchedJournals")

        sample_issns = cast(list[str], d.pop("sampleIssns", UNSET))

        journal_metric_expansion = cls(
            condition=condition,
            field=field,
            issn_count=issn_count,
            matched_journals=matched_journals,
            sample_issns=sample_issns,
        )

        journal_metric_expansion.additional_properties = d
        return journal_metric_expansion

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
