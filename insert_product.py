import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Products')

table.put_item(
    Item={
        'product_id': '121',
        'product_name': 'Laptop',
        'quantity_per_unit': 10,
        'unit_price': 1200
    }
)

print("Product added successfully.")
