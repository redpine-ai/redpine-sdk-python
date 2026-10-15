from enum import Enum


class DiscoveryCollectionItemPriceRangeType0Per(str, Enum):
    VALUE_0 = "1000_tokens"

    def __str__(self) -> str:
        return str(self.value)
