import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'Orders'

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {'AttributeName': 'customer_id', 'KeyType': 'HASH'},  # Partition key
        {'AttributeName': 'order_id', 'KeyType': 'RANGE'}     # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'customer_id', 'AttributeType': 'S'},
        {'AttributeName': 'order_id', 'AttributeType': 'S'},
        {'AttributeName': 'order_date', 'AttributeType': 'S'},
        {'AttributeName': 'shipped_date', 'AttributeType': 'S'},
        {'AttributeName': 'delivery_fee', 'AttributeType': 'N'},
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print(f"Table {table_name} created successfully.")
