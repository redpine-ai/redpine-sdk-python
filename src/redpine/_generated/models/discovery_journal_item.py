from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.discovery_journal_item_kind import DiscoveryJournalItemKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryJournalItem")


@_attrs_define
class DiscoveryJournalItem:
    """
    Attributes:
        kind (DiscoveryJournalItemKind):  Default: DiscoveryJournalItemKind.JOURNAL.
        title (str): Journal title
        h_index (int | None | Unset): h-index (OpenAlex), null when unknown
        impact_factor (float | None | Unset): The journal's journal_metric.impact_factor: an impact factor computed by
            Redpine from OpenAlex citation data with the JIF formula. It is not Clarivate's Journal Impact Factor. Journals
            that publish many news items, letters and editorials (for example BMJ, JAMA, The Lancet) score far below their
            JCR figure, because OpenAlex classifies those items as articles. Null when unknown.
        issn_l (None | str | Unset): Linking ISSN when the journal is known to the metrics table
        issns (list[str] | Unset): The journal's ISSNs present in your scope; filter on these to search it
        publisher (None | str | Unset): Publisher, when known
    """

    title: str
    kind: DiscoveryJournalItemKind = DiscoveryJournalItemKind.JOURNAL
    h_index: int | None | Unset = UNSET
    impact_factor: float | None | Unset = UNSET
    issn_l: None | str | Unset = UNSET
    issns: list[str] | Unset = UNSET
    publisher: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        title = self.title

        h_index: int | None | Unset
        if isinstance(self.h_index, Unset):
            h_index = UNSET
        else:
            h_index = self.h_index

        impact_factor: float | None | Unset
        if isinstance(self.impact_factor, Unset):
            impact_factor = UNSET
        else:
            impact_factor = self.impact_factor

        issn_l: None | str | Unset
        if isinstance(self.issn_l, Unset):
            issn_l = UNSET
        else:
            issn_l = self.issn_l

        issns: list[str] | Unset = UNSET
        if not isinstance(self.issns, Unset):
            issns = self.issns

        publisher: None | str | Unset
        if isinstance(self.publisher, Unset):
            publisher = UNSET
        else:
            publisher = self.publisher

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "title": title,
            }
        )
        if h_index is not UNSET:
            field_dict["hIndex"] = h_index
        if impact_factor is not UNSET:
            field_dict["impactFactor"] = impact_factor
        if issn_l is not UNSET:
            field_dict["issnL"] = issn_l
        if issns is not UNSET:
            field_dict["issns"] = issns
        if publisher is not UNSET:
            field_dict["publisher"] = publisher

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        kind = DiscoveryJournalItemKind(d.pop("kind"))

        title = d.pop("title")

        def _parse_h_index(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        h_index = _parse_h_index(d.pop("hIndex", UNSET))

        def _parse_impact_factor(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        impact_factor = _parse_impact_factor(d.pop("impactFactor", UNSET))

        def _parse_issn_l(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        issn_l = _parse_issn_l(d.pop("issnL", UNSET))

        issns = cast(list[str], d.pop("issns", UNSET))

        def _parse_publisher(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        publisher = _parse_publisher(d.pop("publisher", UNSET))

        discovery_journal_item = cls(
            kind=kind,
            title=title,
            h_index=h_index,
            impact_factor=impact_factor,
            issn_l=issn_l,
            issns=issns,
            publisher=publisher,
        )

        discovery_journal_item.additional_properties = d
        return discovery_journal_item

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
