from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.filter_warning import FilterWarning
    from ..models.journal_metric_expansion import JournalMetricExpansion
    from ..models.search_response_filters_applied_type_0 import SearchResponseFiltersAppliedType0
    from ..models.search_result import SearchResult


T = TypeVar("T", bound="SearchResponse")


@_attrs_define
class SearchResponse:
    """
    Attributes:
        latency_ms (int): Search latency in milliseconds
        query_id (str): Unique identifier for this query. Use it to re-fetch the same results for free within 7 days via
            GET /api/v1/search/results/{queryId}.
        results (list[SearchResult]): Ranked list of matching document chunks.
        filter_warnings (list[FilterWarning] | None | Unset): Advisory warnings about the supplied filter — for example
            filtering on a known field with no payload index, which is matched by scanning, or a collection excluded because
            it holds only open-access content and the filter asked for open_access=false. The search still runs. Omitted
            when there are none.
        filters_applied (None | SearchResponseFiltersAppliedType0 | Unset): The filters you sent, after validation.
            Omitted when no filters were sent.
        journal_metric_expansions (list[JournalMetricExpansion] | None | Unset): How each journal-metric condition
            resolved to ISSNs; omitted when no metric filter was used
    """

    latency_ms: int
    query_id: str
    results: list[SearchResult]
    filter_warnings: list[FilterWarning] | None | Unset = UNSET
    filters_applied: None | SearchResponseFiltersAppliedType0 | Unset = UNSET
    journal_metric_expansions: list[JournalMetricExpansion] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.search_response_filters_applied_type_0 import (
            SearchResponseFiltersAppliedType0,
        )

        latency_ms = self.latency_ms

        query_id = self.query_id

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        filter_warnings: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_warnings, Unset):
            filter_warnings = UNSET
        elif isinstance(self.filter_warnings, list):
            filter_warnings = []
            for filter_warnings_type_0_item_data in self.filter_warnings:
                filter_warnings_type_0_item = filter_warnings_type_0_item_data.to_dict()
                filter_warnings.append(filter_warnings_type_0_item)

        else:
            filter_warnings = self.filter_warnings

        filters_applied: dict[str, Any] | None | Unset
        if isinstance(self.filters_applied, Unset):
            filters_applied = UNSET
        elif isinstance(self.filters_applied, SearchResponseFiltersAppliedType0):
            filters_applied = self.filters_applied.to_dict()
        else:
            filters_applied = self.filters_applied

        journal_metric_expansions: list[dict[str, Any]] | None | Unset
        if isinstance(self.journal_metric_expansions, Unset):
            journal_metric_expansions = UNSET
        elif isinstance(self.journal_metric_expansions, list):
            journal_metric_expansions = []
            for journal_metric_expansions_type_0_item_data in self.journal_metric_expansions:
                journal_metric_expansions_type_0_item = (
                    journal_metric_expansions_type_0_item_data.to_dict()
                )
                journal_metric_expansions.append(journal_metric_expansions_type_0_item)

        else:
            journal_metric_expansions = self.journal_metric_expansions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latencyMs": latency_ms,
                "queryId": query_id,
                "results": results,
            }
        )
        if filter_warnings is not UNSET:
            field_dict["filterWarnings"] = filter_warnings
        if filters_applied is not UNSET:
            field_dict["filtersApplied"] = filters_applied
        if journal_metric_expansions is not UNSET:
            field_dict["journalMetricExpansions"] = journal_metric_expansions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.filter_warning import FilterWarning
        from ..models.journal_metric_expansion import JournalMetricExpansion
        from ..models.search_response_filters_applied_type_0 import (
            SearchResponseFiltersAppliedType0,
        )
        from ..models.search_result import SearchResult

        d = dict(src_dict)
        latency_ms = d.pop("latencyMs")

        query_id = d.pop("queryId")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = SearchResult.from_dict(results_item_data)

            results.append(results_item)

        def _parse_filter_warnings(data: object) -> list[FilterWarning] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_warnings_type_0 = []
                _filter_warnings_type_0 = data
                for filter_warnings_type_0_item_data in _filter_warnings_type_0:
                    filter_warnings_type_0_item = FilterWarning.from_dict(
                        filter_warnings_type_0_item_data
                    )

                    filter_warnings_type_0.append(filter_warnings_type_0_item)

                return filter_warnings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FilterWarning] | None | Unset, data)

        filter_warnings = _parse_filter_warnings(d.pop("filterWarnings", UNSET))

        def _parse_filters_applied(
            data: object,
        ) -> None | SearchResponseFiltersAppliedType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_applied_type_0 = SearchResponseFiltersAppliedType0.from_dict(data)

                return filters_applied_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SearchResponseFiltersAppliedType0 | Unset, data)

        filters_applied = _parse_filters_applied(d.pop("filtersApplied", UNSET))

        def _parse_journal_metric_expansions(
            data: object,
        ) -> list[JournalMetricExpansion] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                journal_metric_expansions_type_0 = []
                _journal_metric_expansions_type_0 = data
                for journal_metric_expansions_type_0_item_data in _journal_metric_expansions_type_0:
                    journal_metric_expansions_type_0_item = JournalMetricExpansion.from_dict(
                        journal_metric_expansions_type_0_item_data
                    )

                    journal_metric_expansions_type_0.append(journal_metric_expansions_type_0_item)

                return journal_metric_expansions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[JournalMetricExpansion] | None | Unset, data)

        journal_metric_expansions = _parse_journal_metric_expansions(
            d.pop("journalMetricExpansions", UNSET)
        )

        search_response = cls(
            latency_ms=latency_ms,
            query_id=query_id,
            results=results,
            filter_warnings=filter_warnings,
            filters_applied=filters_applied,
            journal_metric_expansions=journal_metric_expansions,
        )

        search_response.additional_properties = d
        return search_response

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
