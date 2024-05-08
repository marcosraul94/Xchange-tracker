from datetime import date
from boto3.dynamodb.conditions import Key
from src.entities.bank import Bank
from src.entities.rate import Rate
from src.enums import EntityType, Currency
from src.repositories.base import Repository
from src.utils.serialization import EnumSerialization


class RateRepo(Repository):
    entity = Rate

    def find_by_bank_and_currency(
        self,
        bank: Bank,
        currency: Currency,
    ) -> list[Rate]:
        filter_by_bank = Key("pk").eq(bank.pk)
        filter_by_entity_and_currency = Key("sk").begins_with(
            f"r#{EnumSerialization.serialize(currency)}#"
        )

        response = self.table.query(
            KeyConditionExpression=filter_by_bank
            & filter_by_entity_and_currency,
        )

        return self.deserialize_items(response)

    def find_by_day(self, day: date) -> list[Rate]:
        filter_by_entity = Key("entity_type").eq(EntityType.RATE.value)
        filter_by_day = Key("created_at").begins_with(day.isoformat())

        response = self.table.query(
            IndexName=self.entity_type_index_name,
            KeyConditionExpression=filter_by_entity & filter_by_day,
        )

        return self.deserialize_items(response)
