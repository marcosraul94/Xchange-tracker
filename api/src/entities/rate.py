import uuid
from decimal import Decimal
from src.entities.base import Entity
from src.enums import EntityType, Currency


class Rate(Entity):
    def __init__(
        self,
        pk: str,
        amount: Decimal,
        currency: Currency,
    ):

        self.amount = amount
        self.currency = currency
        super().__init__(
            pk,
            sk=f"r#{uuid.uuid4()}",
            entity_type=EntityType.RATE,
        )

    @classmethod
    def from_serialized(cls, serialized: dict):
        return super().from_serialized(
            serialized,
            constructor_keys=[
                "pk",
                "amount",
                "currency",
            ],
            post_creation_keys=[
                "sk",
                "created_at",
                "updated_at",
            ],
        )
