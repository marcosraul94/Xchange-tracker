import boto3

dynamodb = boto3.resource(
    "dynamodb", endpoint_url="http://db:8000", region_name="us-east-1"
)
print(dynamodb)


def handler(event, context):
    print("Hello world")
