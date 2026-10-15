from enum import Enum


class DiscoveryCalloutKind(str, Enum):
    ADD_PAYMENT_METHOD = "add_payment_method"

    def __str__(self) -> str:
        return str(self.value)
