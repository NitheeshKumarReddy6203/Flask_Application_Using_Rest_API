import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')

table.put_item(
    Item={
        'order_id': '8989',
        'customer_id': '51771',  
        'order_date': '2024-09-01',
        'shipped_date': '2024-09-05',
        'delivery_fee': 5
    }
)
print("Order added successfully.")
