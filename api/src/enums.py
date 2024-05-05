from enum import Enum


class Environment(Enum):
    TEST = "test"
    DEV = "dev"
    PROD = "prod"


class EntityType(Enum):
    BANK = "bank"
    BANK_RATE = "bank rate"
    MIGRATION = "migration"


class Currency(Enum):
    DOLLAR = "dollar"
    EURO = "euro"
