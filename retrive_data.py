# import boto3
# import json
# from decimal import Decimal

# # Set up DynamoDB resource
# dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# # Reference to the DynamoDB table
# table = dynamodb.Table('Customers')

# def convert_decimal(obj):
#     """ Convert Decimal types to float for JSON serialization """
#     if isinstance(obj, Decimal):
#         return float(obj)
#     raise TypeError("Type not serializable")

# def get_customer(customer_id):
#     try:
#         # Fetch the item from the table
#         response = table.get_item(
#             Key={
#                 'CustomerID': customer_id
#             }
#         )

#         # Debugging information
#         print("Response received:")
#         print(json.dumps(response, indent=4, default=convert_decimal))

#         # Check if 'Item' is in the response
#         if 'Item' in response:
#             # Print the customer data
#             print("Customer data:")
#             print(json.dumps(response['Item'], indent=4, default=convert_decimal))
#         else:
#             print(f"Customer with ID {customer_id} not found.")

#     except Exception as e:
#         print(f"Error occurred: {str(e)}")

# if __name__ == '__main__':
#     # Replace 'CUST001' with the actual customer ID you want to retrieve
#     customer_id = 'CUST001'
#     get_customer(customer_id)
# 



# ================================================================================







# import boto3
# import json
# from decimal import Decimal

# # Set up DynamoDB resource
# dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# # Reference to the DynamoDB table
# table = dynamodb.Table('Customers')

# def convert_decimal(obj):
#     """ Convert Decimal types to float for JSON serialization """
#     if isinstance(obj, Decimal):
#         return float(obj)
#     raise TypeError("Type not serializable")

# def get_customer(customer_id):
#     try:
#         # Fetch the item from the table
#         response = table.get_item(
#             Key={
#                 'CustomerID': customer_id
#             }
#         )

#         # Print the customer data
#         if 'Item' in response:
#             print(json.dumps(response['Item'], indent=4, default=convert_decimal))
#         else:
#             print(f"Customer with ID {customer_id} not found.")

#     except Exception as e:
#         print(f"Error occurred: {str(e)}")

# if __name__ == '__main__':
#     # Replace 'CUST001' with the actual customer ID you want to retrieve
#     customer_id = 'CUST001'
#     get_customer(customer_id)





# ================================================================================





import boto3
import json
from decimal import Decimal

# Set up DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# Reference to the DynamoDB table
table = dynamodb.Table('Customers')

def convert_decimal(obj):
    """ Convert Decimal types to float or int for JSON serialization """
    if isinstance(obj, Decimal):
        # Convert Decimal to integer if it has no fractional part, otherwise to float
        if obj % 1 == 0:
            return int(obj)
        return float(obj)
    raise TypeError("Type not serializable")

def get_customer(customer_id):
    try:
        # Fetch the item from the table
        response = table.get_item(
            Key={
                'CustomerID': customer_id
            }
        )

        # Print the customer data
        if 'Item' in response:
            print(json.dumps(response['Item'], indent=4, default=convert_decimal))
        else:
            print(f"Customer with ID {customer_id} not found.")

    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    # Replace 'CUST001' with the actual customer ID you want to retrieve
    customer_id = 'CUST001'
    get_customer(customer_id)
