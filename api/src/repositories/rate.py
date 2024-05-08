from datetime import date
from boto3.dynamodb.conditions import Key
from src.enums import EntityType
from src.entities.bank import Bank
from src.entities.rate import Rate
from src.repositories.base import Repository


class RateRepo(Repository):
    entity = Rate

    def find_by_bank(self, bank: Bank) -> list[Rate]:
        response = self.table.query(
            KeyConditionExpression=Key("pk").eq(bank.pk)
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
