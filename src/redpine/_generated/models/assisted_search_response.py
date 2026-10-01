from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.assisted_search_response_status import AssistedSearchResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.assisted_billing_info import AssistedBillingInfo
    from ..models.assisted_search_result import AssistedSearchResult
    from ..models.clarification_info import ClarificationInfo
    from ..models.filter_warning import FilterWarning
    from ..models.journal_metric_expansion import JournalMetricExpansion
    from ..models.query_understanding import QueryUnderstanding


T = TypeVar("T", bound="AssistedSearchResponse")


@_attrs_define
class AssistedSearchResponse:
    """
    Attributes:
        billing (AssistedBillingInfo): What was actually charged — only delivered, verified results are billed.
        iterations_run (int): Number of search+replan rounds executed
        latency_ms (int): End-to-end latency in milliseconds
        query_id (str): Query ID for audit reference
        query_understanding (QueryUnderstanding): How the endpoint read the query.
        status (AssistedSearchResponseStatus): Outcome of the assisted search
        clarification (ClarificationInfo | None | Unset): Set only when status is `clarification_needed`.
        filter_warnings (list[FilterWarning] | None | Unset): Advisory warnings about the supplied filter — for example
            filtering on a known field with no payload index, which is matched by scanning, or a collection excluded because
            it holds only open-access content and the filter asked for open_access=false. The search still runs. Omitted
            when there are none.
        journal_metric_expansions (list[JournalMetricExpansion] | None | Unset): How each journal-metric condition
            resolved to ISSNs; omitted when no metric filter was used
        results (list[AssistedSearchResult] | Unset): Verified results (empty unless status='results')
    """

    billing: AssistedBillingInfo
    iterations_run: int
    latency_ms: int
    query_id: str
    query_understanding: QueryUnderstanding
    status: AssistedSearchResponseStatus
    clarification: ClarificationInfo | None | Unset = UNSET
    filter_warnings: list[FilterWarning] | None | Unset = UNSET
    journal_metric_expansions: list[JournalMetricExpansion] | None | Unset = UNSET
    results: list[AssistedSearchResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.clarification_info import ClarificationInfo

        billing = self.billing.to_dict()

        iterations_run = self.iterations_run

        latency_ms = self.latency_ms

        query_id = self.query_id

        query_understanding = self.query_understanding.to_dict()

        status = self.status.value

        clarification: dict[str, Any] | None | Unset
        if isinstance(self.clarification, Unset):
            clarification = UNSET
        elif isinstance(self.clarification, ClarificationInfo):
            clarification = self.clarification.to_dict()
        else:
            clarification = self.clarification

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

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "billing": billing,
                "iterationsRun": iterations_run,
                "latencyMs": latency_ms,
                "queryId": query_id,
                "queryUnderstanding": query_understanding,
                "status": status,
            }
        )
        if clarification is not UNSET:
            field_dict["clarification"] = clarification
        if filter_warnings is not UNSET:
            field_dict["filterWarnings"] = filter_warnings
        if journal_metric_expansions is not UNSET:
            field_dict["journalMetricExpansions"] = journal_metric_expansions
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.assisted_billing_info import AssistedBillingInfo
        from ..models.assisted_search_result import AssistedSearchResult
        from ..models.clarification_info import ClarificationInfo
        from ..models.filter_warning import FilterWarning
        from ..models.journal_metric_expansion import JournalMetricExpansion
        from ..models.query_understanding import QueryUnderstanding

        d = dict(src_dict)
        billing = AssistedBillingInfo.from_dict(d.pop("billing"))

        iterations_run = d.pop("iterationsRun")

        latency_ms = d.pop("latencyMs")

        query_id = d.pop("queryId")

        query_understanding = QueryUnderstanding.from_dict(d.pop("queryUnderstanding"))

        status = AssistedSearchResponseStatus(d.pop("status"))

        def _parse_clarification(data: object) -> ClarificationInfo | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                clarification_type_0 = ClarificationInfo.from_dict(data)

                return clarification_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ClarificationInfo | None | Unset, data)

        clarification = _parse_clarification(d.pop("clarification", UNSET))

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

        _results = d.pop("results", UNSET)
        results: list[AssistedSearchResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = AssistedSearchResult.from_dict(results_item_data)

                results.append(results_item)

        assisted_search_response = cls(
            billing=billing,
            iterations_run=iterations_run,
            latency_ms=latency_ms,
            query_id=query_id,
            query_understanding=query_understanding,
            status=status,
            clarification=clarification,
            filter_warnings=filter_warnings,
            journal_metric_expansions=journal_metric_expansions,
            results=results,
        )

        assisted_search_response.additional_properties = d
        return assisted_search_response

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
