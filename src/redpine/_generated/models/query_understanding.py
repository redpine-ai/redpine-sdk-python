from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_understanding_filters import QueryUnderstandingFilters


T = TypeVar("T", bound="QueryUnderstanding")


@_attrs_define
class QueryUnderstanding:
    """How the endpoint read the query.

    Attributes:
        aspects (list[str] | Unset): Facets asked about the entity (e.g. mechanism of action, dermal penetration,
            clinical outcomes)
        entities (list[str] | Unset): Entities the query is about (substances, genes, diseases, organisms, methods)
        filters (QueryUnderstandingFilters | Unset): Structured metadata constraints read off the query. Possible keys
            (snake_case, present only when the query named the constraint): 'journal' (str), 'publisher' (str),
            'article_type' (str, JATS vocabulary), 'publication_date' ({'gte'?: 'YYYY-MM-DD', 'lt'?: 'YYYY-MM-DD'}). Empty
            object when the query named none.
        intent (str | Unset): What the query is asking for Default: ''.
    """

    aspects: list[str] | Unset = UNSET
    entities: list[str] | Unset = UNSET
    filters: QueryUnderstandingFilters | Unset = UNSET
    intent: str | Unset = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspects: list[str] | Unset = UNSET
        if not isinstance(self.aspects, Unset):
            aspects = self.aspects

        entities: list[str] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        intent = self.intent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspects is not UNSET:
            field_dict["aspects"] = aspects
        if entities is not UNSET:
            field_dict["entities"] = entities
        if filters is not UNSET:
            field_dict["filters"] = filters
        if intent is not UNSET:
            field_dict["intent"] = intent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.query_understanding_filters import QueryUnderstandingFilters

        d = dict(src_dict)
        aspects = cast(list[str], d.pop("aspects", UNSET))

        entities = cast(list[str], d.pop("entities", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: QueryUnderstandingFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = QueryUnderstandingFilters.from_dict(_filters)

        intent = d.pop("intent", UNSET)

        query_understanding = cls(
            aspects=aspects,
            entities=entities,
            filters=filters,
            intent=intent,
        )

        query_understanding.additional_properties = d
        return query_understanding

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
