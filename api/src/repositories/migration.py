from boto3.dynamodb.conditions import Key
from src.repositories.base import Repository
from src.entities.migration import Migration


class MigrationRepo(Repository):
    def find_all(self) -> list[Migration]:
        response = self.table.query(KeyConditionExpression=Key("pk").eq("m#"))
        items = response.get("Items", [])

        return [Migration.from_serialized(item) for item in items]
