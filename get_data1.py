import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Define the table
table = dynamodb.Table('Customer')

def get_customer(customer_id):
    try:
        response = table.get_item(
            Key={'customer_id': int(customer_id)}
        )
        return response['Item']
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    customer_id = 51771  # Example customer_id
    customer_data = get_customer(customer_id)
    print(customer_data)
