import boto3
import os

dynamodb_client = boto3.client('dynamodb', region_name='ap-south-1')
dynamodb_resource = boto3.resource('dynamodb')

