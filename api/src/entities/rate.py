from decimal import Decimal
from src.entities.base import Entity
from src.enums import EntityType, Currency
from src.utils.serialization import DateSerialization, EnumSerialization


class Rate(Entity):
    def __init__(
        self,
        bank_name: str,
        amount: Decimal,
        currency: Currency,
    ):
        super().__init__(
            pk=f"b#{bank_name}",
            sk=None,
            entity_type=EntityType.RATE,
        )

        self.amount = amount
        self.currency = currency
        self.bank_name = bank_name

        created_at = DateSerialization.serialize(self.created_at.date())
        currency = EnumSerialization.serialize(currency)
        self.sk = f"r#{currency}#{created_at}"

    @classmethod
    def from_serialized(cls, serialized: dict):
        return super().from_serialized(
            serialized,
            constructor_keys=[
                "bank_name",
                "amount",
                "currency",
            ],
            post_creation_keys=[
                "sk",
                "created_at",
                "updated_at",
            ],
        )
