import boto3
from botocore.exceptions import ClientError

# Set up DynamoDB connection (Assumes AWS credentials and region are configured)
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
customer_table = dynamodb.Table('Customers')  # Ensure this matches your DynamoDB table name

def update_customer(customer_id, update_data):
    try:
        update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in update_data.keys()])
        expression_attribute_values = {f":{k}": v for k, v in update_data.items()}

        response = customer_table.update_item(
            Key={'customer_id': customer_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues="UPDATED_NEW"
        )

        return response['Attributes']

    except ClientError as e:
        print(f"Error updating customer: {e}")
        return None

# Test the function
if __name__ == '__main__':
    customer_id = '12345' 
    update_data = {
        'customer_name': 'NKR',
        'customer_title': 'Engineer',
        'customer_address': 'Block 1, Mg Road'
    }

    updated_customer = update_customer(customer_id, update_data)
    
    if updated_customer:
        print("Customer updated successfully:", updated_customer)
    else:
        print("Failed to update customer.")
