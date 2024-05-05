from decimal import Decimal
from src.entities.base import Entity
from src.enums import EntityType, Currency


class BankRate(Entity):
    def __init__(
        self,
        pk: str,
        sk: str,
        amount: Decimal,
        currency: Currency,
    ):
        self.amount = amount
        self.currency = currency
        super().__init__(pk, sk, entity_type=EntityType.BANK)
