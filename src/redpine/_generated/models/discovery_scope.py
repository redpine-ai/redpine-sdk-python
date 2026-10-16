from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_collection_item import DiscoveryCollectionItem
    from ..models.discovery_journal_item import DiscoveryJournalItem
    from ..models.discovery_publisher_item import DiscoveryPublisherItem


T = TypeVar("T", bound="DiscoveryScope")


@_attrs_define
class DiscoveryScope:
    """
    Attributes:
        collection (str): The requested collection name
        display_name (str): Display name of the requested collection
        total (int): Proved distinct journals (or items) in this scope
        issn_values_seen (int | Unset): Raw distinct ISSN values seen in your scope Default: 0.
        items (list[DiscoveryCollectionItem | DiscoveryJournalItem | DiscoveryPublisherItem] | Unset): Ranked items; the
            `kind` of each says which shape it is.
        note (None | str | Unset): A caveat about this block, when any
        offset (int | Unset): Rank of the first item in this page, zero-based Default: 0.
        publishers (list[str] | Unset): Publishers present in your scope of this collection
        ranked_by (None | str | Unset): How items are ordered: `h_index` or `relevant_content`; null when the items are
            not ranked
        sampled_entries (int | Unset): ISSN groups seen in the corpus but unknown to the metrics table; never counted as
            proved journals Default: 0.
        shown (int | Unset): Items in this page (and rendered in the text form) Default: 0.
        title_only (int | Unset): Journals known only by a title (points with no ISSN) Default: 0.
        truncated_inventory (bool | Unset): True when the inventory is incomplete (limits or deadline) Default: False.
        unranked (list[DiscoveryJournalItem] | Unset): Journals with no metrics (sampled or title-only entries); never
            ranked
        unresolved_issns (int | Unset): ISSNs that could not be resolved to a title Default: 0.
    """

    collection: str
    display_name: str
    total: int
    issn_values_seen: int | Unset = 0
    items: list[DiscoveryCollectionItem | DiscoveryJournalItem | DiscoveryPublisherItem] | Unset = (
        UNSET
    )
    note: None | str | Unset = UNSET
    offset: int | Unset = 0
    publishers: list[str] | Unset = UNSET
    ranked_by: None | str | Unset = UNSET
    sampled_entries: int | Unset = 0
    shown: int | Unset = 0
    title_only: int | Unset = 0
    truncated_inventory: bool | Unset = False
    unranked: list[DiscoveryJournalItem] | Unset = UNSET
    unresolved_issns: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discovery_collection_item import DiscoveryCollectionItem
        from ..models.discovery_journal_item import DiscoveryJournalItem

        collection = self.collection

        display_name = self.display_name

        total = self.total

        issn_values_seen = self.issn_values_seen

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item: dict[str, Any]
                if isinstance(items_item_data, DiscoveryJournalItem) or isinstance(
                    items_item_data, DiscoveryCollectionItem
                ):
                    items_item = items_item_data.to_dict()
                else:
                    items_item = items_item_data.to_dict()

                items.append(items_item)

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        offset = self.offset

        publishers: list[str] | Unset = UNSET
        if not isinstance(self.publishers, Unset):
            publishers = self.publishers

        ranked_by: None | str | Unset
        if isinstance(self.ranked_by, Unset):
            ranked_by = UNSET
        else:
            ranked_by = self.ranked_by

        sampled_entries = self.sampled_entries

        shown = self.shown

        title_only = self.title_only

        truncated_inventory = self.truncated_inventory

        unranked: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unranked, Unset):
            unranked = []
            for unranked_item_data in self.unranked:
                unranked_item = unranked_item_data.to_dict()
                unranked.append(unranked_item)

        unresolved_issns = self.unresolved_issns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection": collection,
                "displayName": display_name,
                "total": total,
            }
        )
        if issn_values_seen is not UNSET:
            field_dict["issnValuesSeen"] = issn_values_seen
        if items is not UNSET:
            field_dict["items"] = items
        if note is not UNSET:
            field_dict["note"] = note
        if offset is not UNSET:
            field_dict["offset"] = offset
        if publishers is not UNSET:
            field_dict["publishers"] = publishers
        if ranked_by is not UNSET:
            field_dict["rankedBy"] = ranked_by
        if sampled_entries is not UNSET:
            field_dict["sampledEntries"] = sampled_entries
        if shown is not UNSET:
            field_dict["shown"] = shown
        if title_only is not UNSET:
            field_dict["titleOnly"] = title_only
        if truncated_inventory is not UNSET:
            field_dict["truncatedInventory"] = truncated_inventory
        if unranked is not UNSET:
            field_dict["unranked"] = unranked
        if unresolved_issns is not UNSET:
            field_dict["unresolvedIssns"] = unresolved_issns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.discovery_collection_item import DiscoveryCollectionItem
        from ..models.discovery_journal_item import DiscoveryJournalItem
        from ..models.discovery_publisher_item import DiscoveryPublisherItem

        d = dict(src_dict)
        collection = d.pop("collection")

        display_name = d.pop("displayName")

        total = d.pop("total")

        issn_values_seen = d.pop("issnValuesSeen", UNSET)

        _items = d.pop("items", UNSET)
        items: (
            list[DiscoveryCollectionItem | DiscoveryJournalItem | DiscoveryPublisherItem] | Unset
        ) = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:

                def _parse_items_item(
                    data: object,
                ) -> DiscoveryCollectionItem | DiscoveryJournalItem | DiscoveryPublisherItem:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_item_type_0 = DiscoveryJournalItem.from_dict(data)

                        return items_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        items_item_type_1 = DiscoveryCollectionItem.from_dict(data)

                        return items_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_item_type_2 = DiscoveryPublisherItem.from_dict(data)

                    return items_item_type_2

                items_item = _parse_items_item(items_item_data)

                items.append(items_item)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        offset = d.pop("offset", UNSET)

        publishers = cast(list[str], d.pop("publishers", UNSET))

        def _parse_ranked_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ranked_by = _parse_ranked_by(d.pop("rankedBy", UNSET))

        sampled_entries = d.pop("sampledEntries", UNSET)

        shown = d.pop("shown", UNSET)

        title_only = d.pop("titleOnly", UNSET)

        truncated_inventory = d.pop("truncatedInventory", UNSET)

        _unranked = d.pop("unranked", UNSET)
        unranked: list[DiscoveryJournalItem] | Unset = UNSET
        if _unranked is not UNSET:
            unranked = []
            for unranked_item_data in _unranked:
                unranked_item = DiscoveryJournalItem.from_dict(unranked_item_data)

                unranked.append(unranked_item)

        unresolved_issns = d.pop("unresolvedIssns", UNSET)

        discovery_scope = cls(
            collection=collection,
            display_name=display_name,
            total=total,
            issn_values_seen=issn_values_seen,
            items=items,
            note=note,
            offset=offset,
            publishers=publishers,
            ranked_by=ranked_by,
            sampled_entries=sampled_entries,
            shown=shown,
            title_only=title_only,
            truncated_inventory=truncated_inventory,
            unranked=unranked,
            unresolved_issns=unresolved_issns,
        )

        discovery_scope.additional_properties = d
        return discovery_scope

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
