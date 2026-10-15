from enum import Enum


class DiscoveryScopeRankedByType2Type1(str, Enum):
    H_INDEX = "h_index"
    RELEVANT_CONTENT = "relevant_content"

    def __str__(self) -> str:
        return str(self.value)
