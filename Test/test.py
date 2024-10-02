import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customers')

def get_customer(customer_id):
    response = table.get_item(
        Key={'customer_id': str(customer_id)}  
    )
    item = response.get('Item')
    if item:
        item = {k: (int(v) if isinstance(v, Decimal) else v) for k, v in item.items()}
    return item

customer_id = '62030'  
customer_data = get_customer(customer_id)
print(customer_data)
