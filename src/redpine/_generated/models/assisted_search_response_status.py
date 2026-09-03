from enum import Enum


class AssistedSearchResponseStatus(str, Enum):
    CLARIFICATION_NEEDED = "clarification_needed"
    NO_RELEVANT_RESULTS = "no_relevant_results"
    RESULTS = "results"

    def __str__(self) -> str:
        return str(self.value)
