import boto3

dynamodb = boto3.resource('dynamodb')

table_name = 'Products'

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {'AttributeName': 'product_id', 'KeyType': 'HASH'},  # Partition key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'product_id', 'AttributeType': 'S'}, # String type for product_id
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
) 

table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

print(f"Table {table_name} created successfully.")
