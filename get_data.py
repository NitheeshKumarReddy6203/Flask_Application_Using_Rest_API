import boto3

def get_customer(customer_id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table = dynamodb.Table('Customers')

    try:
        response = table.get_item(Key={'customer_id': customer_id})
        if 'Item' in response:
            return response['Item']
        else:
            print(f"No customer found with customer_id: {customer_id}")
    except Exception as e:
        print(e)

customer_data = get_customer(51771)
print(customer_data)
