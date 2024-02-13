import boto3
from .env import dynamo_endpoint, aws_region, aws_access_key_id, aws_secret_access_key


class DynamoDB:
    def __init__(self) -> None:
        self.client = boto3.resource(
            "dynamodb",
            endpoint_url=dynamo_endpoint,
            region_name=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
