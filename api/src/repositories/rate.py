from boto3.dynamodb.conditions import Key
from src.entities.bank import Bank
from src.repositories.base import Repository
from src.enums import EntityType


class BankRateRepo(Repository):
    def find_by_bank(self):
        response = self.table.query(
            IndexName=self.entity_type_index_name,
            KeyConditionExpression=Key("entity_type").eq(
                EntityType.BANK.value
            ),
        )
        items = response.get("Items", [])

        return [Bank.from_serialized(item) for item in items]
    
    def find_by_bank(self):
        response = self.table.query(
            IndexName=self.entity_type_index_name,
            KeyConditionExpression=Key("entity_type").eq(
                EntityType.BANK.value
            ),
        )
        items = response.get("Items", [])

        return [Bank.from_serialized(item) for item in items]
