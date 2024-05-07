from src.db import get_client


def migrate():
    client = get_client()
    table = client.Table("exchange_tracker")
    table.update(
        AttributeDefinitions=[
            {"AttributeName": "entity_type", "AttributeType": "S"},
            {"AttributeName": "created_at", "AttributeType": "S"},
            {"AttributeName": "updated_at", "AttributeType": "S"},
        ],
        GlobalSecondaryIndexUpdates=[
            {
                "Create": {
                    "IndexName": "entity_type_gsi",
                    "KeySchema": [
                        {
                            "AttributeName": "entity_type",
                            "KeyType": "HASH",
                        },
                        {
                            "AttributeName": "created_at",
                            "KeyType": "RANGE",
                        },
                    ],
                    "Projection": {"ProjectionType": "ALL"},
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 5,
                        "WriteCapacityUnits": 5,
                    },
                },
            },
        ],
    )
