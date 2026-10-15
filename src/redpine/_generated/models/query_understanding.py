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
        case_summary (str | Unset): For a long query such as a patient case: the summary the results were judged
            against. Empty for an ordinary query. Default: ''.
        entities (list[str] | Unset): Entities the query is about (substances, genes, diseases, organisms, methods)
        filters (QueryUnderstandingFilters | Unset): Structured metadata constraints read off the query. Possible keys
            (snake_case, present only when the query named the constraint): 'journal' (str), 'publisher' (str),
            'article_type' (str, JATS vocabulary), 'publication_date' ({'gte'?: 'YYYY-MM-DD', 'lt'?: 'YYYY-MM-DD'}). Empty
            object when the query named none.
        intent (str | Unset): What the query is asking for Default: ''.
        sub_questions (list[str] | Unset): The separate problems a long query was split into, each searched and given
            result slots on its own. Empty for a single-question query.
    """

    aspects: list[str] | Unset = UNSET
    case_summary: str | Unset = ""
    entities: list[str] | Unset = UNSET
    filters: QueryUnderstandingFilters | Unset = UNSET
    intent: str | Unset = ""
    sub_questions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspects: list[str] | Unset = UNSET
        if not isinstance(self.aspects, Unset):
            aspects = self.aspects

        case_summary = self.case_summary

        entities: list[str] | Unset = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        intent = self.intent

        sub_questions: list[str] | Unset = UNSET
        if not isinstance(self.sub_questions, Unset):
            sub_questions = self.sub_questions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspects is not UNSET:
            field_dict["aspects"] = aspects
        if case_summary is not UNSET:
            field_dict["caseSummary"] = case_summary
        if entities is not UNSET:
            field_dict["entities"] = entities
        if filters is not UNSET:
            field_dict["filters"] = filters
        if intent is not UNSET:
            field_dict["intent"] = intent
        if sub_questions is not UNSET:
            field_dict["subQuestions"] = sub_questions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.query_understanding_filters import QueryUnderstandingFilters

        d = dict(src_dict)
        aspects = cast(list[str], d.pop("aspects", UNSET))

        case_summary = d.pop("caseSummary", UNSET)

        entities = cast(list[str], d.pop("entities", UNSET))

        _filters = d.pop("filters", UNSET)
        filters: QueryUnderstandingFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = QueryUnderstandingFilters.from_dict(_filters)

        intent = d.pop("intent", UNSET)

        sub_questions = cast(list[str], d.pop("subQuestions", UNSET))

        query_understanding = cls(
            aspects=aspects,
            case_summary=case_summary,
            entities=entities,
            filters=filters,
            intent=intent,
            sub_questions=sub_questions,
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
