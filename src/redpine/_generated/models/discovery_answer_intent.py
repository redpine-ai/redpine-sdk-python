from enum import Enum


class DiscoveryAnswerIntent(str, Enum):
    JOURNALS = "journals"
    PUBLISHERS = "publishers"
    SOURCES = "sources"

    def __str__(self) -> str:
        return str(self.value)
