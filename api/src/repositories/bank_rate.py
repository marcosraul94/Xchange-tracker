from boto3.dynamodb.conditions import Key
from src.entities.bank import Bank
from src.repositories.base import Repository


class BankRepo(Repository):
    def find_all(self):
        response = self.table.query(KeyConditionExpression=Key("pk").eq("b#"))
        items = response.get("Items", [])

        return [Bank.from_serialized(item) for item in items]
