import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customers')

table.put_item(
    Item={
        'customer_id': '51771',
        'customer_name': 'Reddy',
        'customer_title': 'Intern Research',
        'customer_phone_number': 9876511110,
        'customer_address':'Bnglr - 560045'
    }
)

print("Customer added successfully.")
