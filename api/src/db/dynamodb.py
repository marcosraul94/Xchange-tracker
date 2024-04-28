import boto3
import src.env as env


class DynamoDB:
    def __init__(self) -> None:
        self.client = boto3.resource(
            "dynamodb",
            endpoint_url=env.dynamo_endpoint,
            region_name=env.aws_region,
            aws_access_key_id=env.aws_access_key_id,
            aws_secret_access_key=env.aws_secret_access_key,
        )
