import boto3
from src.constants import (
    dynamo_endpoint,
    aws_region,
    aws_access_key_id,
    aws_secret_access_key,
)

_db = None


def get_client():
    global _db

    if not _db:
        _db = boto3.resource(
            "dynamodb",
            endpoint_url=dynamo_endpoint,
            region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )

    return _db
