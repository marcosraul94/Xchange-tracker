from attrs import define
from decimal import Decimal
from .base import Entity
from src.constants import EntityType


@define
class BankRate(Entity):
    amount: Decimal
    entity_type = EntityType.BANK_RATE.value