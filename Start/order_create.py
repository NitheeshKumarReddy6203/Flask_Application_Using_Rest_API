import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'Orders'

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {'AttributeName': 'order_id', 'KeyType': 'HASH'}, 
    ],
    AttributeDefinitions=[
        {'AttributeName': 'order_id', 'AttributeType': 'S'} 
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print(f"Table {table_name} created successfully.")
