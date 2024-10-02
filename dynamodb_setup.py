import boto3
import os

aws_access_key_id = os.getenv('AKIASIVGK4BWSJKUAZL7')
aws_secret_access_key = os.getenv('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')
region_name = 'ap-south-1'  

dynamodb_client = boto3.client('dynamodb', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)
dynamodb_resource = boto3.resource('dynamodb', 
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)
