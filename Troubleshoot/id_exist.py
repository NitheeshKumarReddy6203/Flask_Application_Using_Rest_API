import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customers')

response = table.get_item(Key={'customer_id': 62030})
print(response)
