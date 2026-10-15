from enum import Enum


class DiscoveryPublisherItemKind(str, Enum):
    PUBLISHER = "publisher"

    def __str__(self) -> str:
        return str(self.value)
