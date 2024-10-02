import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Customers')

def insert_customer(customer_id, name, address, phone_number, title):
    response = table.put_item(
        Item={
            'customer_id': str(customer_id),  # Ensure it's a string
            'customer_name': name,
            'customer_address': address,
            'customer_phone_number': phone_number,
            'customer_title': title
        }
    )
    return response

# Example usage
response = insert_customer(62030, 'Nitheesh', 'Bnglr - 562112', 9876543210, 'Intern')
print(response)
