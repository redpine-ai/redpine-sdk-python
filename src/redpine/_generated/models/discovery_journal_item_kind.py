from enum import Enum


class DiscoveryJournalItemKind(str, Enum):
    JOURNAL = "journal"

    def __str__(self) -> str:
        return str(self.value)
