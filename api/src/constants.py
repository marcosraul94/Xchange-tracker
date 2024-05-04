import os
from enum import Enum


class EntityType(Enum):
    BANK = "bank"
    BANK_RATE = "bank rate"
    MIGRATION = "migration"


class Currency(Enum):
    DOLLAR = "dollar"
    EURO = "euro"


table_name = "exchange_tracker"

migrations_path = os.path.join(os.getcwd(), "migrations")
