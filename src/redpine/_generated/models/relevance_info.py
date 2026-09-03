from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RelevanceInfo")


@_attrs_define
class RelevanceInfo:
    """Why a result was judged relevant.

    Attributes:
        judge_score (float): Relevance score assigned by the judge (0..1)
        matched_terms (list[str] | Unset): Entity/synonym surface forms found in the chunk (for highlighting)
        rationale (str | Unset): One-sentence explanation of relevance Default: ''.
    """

    judge_score: float
    matched_terms: list[str] | Unset = UNSET
    rationale: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        judge_score = self.judge_score

        matched_terms: list[str] | Unset = UNSET
        if not isinstance(self.matched_terms, Unset):
            matched_terms = self.matched_terms

        rationale = self.rationale

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "judgeScore": judge_score,
            }
        )
        if matched_terms is not UNSET:
            field_dict["matchedTerms"] = matched_terms
        if rationale is not UNSET:
            field_dict["rationale"] = rationale

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        judge_score = d.pop("judgeScore")

        matched_terms = cast(list[str], d.pop("matchedTerms", UNSET))

        rationale = d.pop("rationale", UNSET)

        relevance_info = cls(
            judge_score=judge_score,
            matched_terms=matched_terms,
            rationale=rationale,
        )

        relevance_info.additional_properties = d
        return relevance_info

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
