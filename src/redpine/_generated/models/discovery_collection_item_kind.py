from enum import Enum


class DiscoveryCollectionItemKind(str, Enum):
    COLLECTION = "collection"

    def __str__(self) -> str:
        return str(self.value)
