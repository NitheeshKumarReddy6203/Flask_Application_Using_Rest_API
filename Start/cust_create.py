import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'Customers'

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {'AttributeName': 'customer_id', 'KeyType': 'HASH'}, 
    ],
    AttributeDefinitions=[
        {'AttributeName': 'customer_id', 'AttributeType': 'S'},  # For the partition key
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print(f"Table {table_name} created successfully.")
