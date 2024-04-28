from .base import View
from src.db.client import dynamodb


class GetBanksRates(View):
    def __init__(self) -> None:
        pass

    def render(self):
        table = dynamodb.client.create_table(
            TableName="testing",
            KeySchema=[
                {"AttributeName": "year", "KeyType": "HASH"},  # Partition key
                {"AttributeName": "title", "KeyType": "RANGE"},  # Sort key
            ],
            AttributeDefinitions=[
                {"AttributeName": "year", "AttributeType": "N"},
                {"AttributeName": "title", "AttributeType": "S"},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 10,
                "WriteCapacityUnits": 10,
            },
        )
        table.wait_until_exists()

        print("I am here", list(dynamodb.client.tables.all()))

        return self.format_response("Hello world")


class CreateBanksRates(View):
    def __init__(self) -> None:
        pass

    def render():
        pass
