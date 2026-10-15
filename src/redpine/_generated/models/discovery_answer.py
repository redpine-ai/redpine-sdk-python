from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.discovery_answer_intent import DiscoveryAnswerIntent
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.discovery_callout import DiscoveryCallout
    from ..models.discovery_next_action import DiscoveryNextAction
    from ..models.discovery_scope import DiscoveryScope


T = TypeVar("T", bound="DiscoveryAnswer")


@_attrs_define
class DiscoveryAnswer:
    """A catalogue answer: what data sources, publishers or journals your key can reach. Present only when the query asked
    about the catalogue rather than for literature; then `results` is empty and nothing was charged (`X-Query-Cost:
    0.000000`).

        Attributes:
            intent (DiscoveryAnswerIntent): Which catalogue question was answered
            query_id (str): Audit reference (disc_…)
            text (str): Pre-rendered text form (what MCP shows)
            callout (DiscoveryCallout | None | Unset): Set when there is a notice (today: add a payment method to unlock
                licensed journals).
            metrics_note (None | str | Unset): How to read the h-index and IF figures; set whenever metrics are shown
            next_actions (list[DiscoveryNextAction] | Unset):
            scopes (list[DiscoveryScope] | Unset): One block per collection
            topic (None | str | Unset): Topic, for a topic-scoped journals answer
    """

    intent: DiscoveryAnswerIntent
    query_id: str
    text: str
    callout: DiscoveryCallout | None | Unset = UNSET
    metrics_note: None | str | Unset = UNSET
    next_actions: list[DiscoveryNextAction] | Unset = UNSET
    scopes: list[DiscoveryScope] | Unset = UNSET
    topic: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discovery_callout import DiscoveryCallout

        intent = self.intent.value

        query_id = self.query_id

        text = self.text

        callout: dict[str, Any] | None | Unset
        if isinstance(self.callout, Unset):
            callout = UNSET
        elif isinstance(self.callout, DiscoveryCallout):
            callout = self.callout.to_dict()
        else:
            callout = self.callout

        metrics_note: None | str | Unset
        if isinstance(self.metrics_note, Unset):
            metrics_note = UNSET
        else:
            metrics_note = self.metrics_note

        next_actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.next_actions, Unset):
            next_actions = []
            for next_actions_item_data in self.next_actions:
                next_actions_item = next_actions_item_data.to_dict()
                next_actions.append(next_actions_item)

        scopes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = []
            for scopes_item_data in self.scopes:
                scopes_item = scopes_item_data.to_dict()
                scopes.append(scopes_item)

        topic: None | str | Unset
        if isinstance(self.topic, Unset):
            topic = UNSET
        else:
            topic = self.topic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intent": intent,
                "queryId": query_id,
                "text": text,
            }
        )
        if callout is not UNSET:
            field_dict["callout"] = callout
        if metrics_note is not UNSET:
            field_dict["metricsNote"] = metrics_note
        if next_actions is not UNSET:
            field_dict["nextActions"] = next_actions
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if topic is not UNSET:
            field_dict["topic"] = topic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.discovery_callout import DiscoveryCallout
        from ..models.discovery_next_action import DiscoveryNextAction
        from ..models.discovery_scope import DiscoveryScope

        d = dict(src_dict)
        intent = DiscoveryAnswerIntent(d.pop("intent"))

        query_id = d.pop("queryId")

        text = d.pop("text")

        def _parse_callout(data: object) -> DiscoveryCallout | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                callout_type_0 = DiscoveryCallout.from_dict(data)

                return callout_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiscoveryCallout | None | Unset, data)

        callout = _parse_callout(d.pop("callout", UNSET))

        def _parse_metrics_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metrics_note = _parse_metrics_note(d.pop("metricsNote", UNSET))

        _next_actions = d.pop("nextActions", UNSET)
        next_actions: list[DiscoveryNextAction] | Unset = UNSET
        if _next_actions is not UNSET:
            next_actions = []
            for next_actions_item_data in _next_actions:
                next_actions_item = DiscoveryNextAction.from_dict(next_actions_item_data)

                next_actions.append(next_actions_item)

        _scopes = d.pop("scopes", UNSET)
        scopes: list[DiscoveryScope] | Unset = UNSET
        if _scopes is not UNSET:
            scopes = []
            for scopes_item_data in _scopes:
                scopes_item = DiscoveryScope.from_dict(scopes_item_data)

                scopes.append(scopes_item)

        def _parse_topic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        topic = _parse_topic(d.pop("topic", UNSET))

        discovery_answer = cls(
            intent=intent,
            query_id=query_id,
            text=text,
            callout=callout,
            metrics_note=metrics_note,
            next_actions=next_actions,
            scopes=scopes,
            topic=topic,
        )

        discovery_answer.additional_properties = d
        return discovery_answer

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
