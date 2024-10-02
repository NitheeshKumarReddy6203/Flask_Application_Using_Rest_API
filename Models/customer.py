from dynamodb_setup import dynamodb_resource
from botocore.exceptions import ClientError

customer_table = dynamodb_resource.Table('Customers')

class Customers:
    def __init__(self, customer_id, customer_name, customer_title=None, customer_phone_number=None, customer_address=None):
        self.customer_id = str(customer_id)
        self.customer_name = customer_name
        self.customer_title = customer_title
        self.customer_phone_number = customer_phone_number
        self.customer_address = customer_address

    def save(self):
        customer_table.put_item(Item={
            'customer_id': self.customer_id,
            'customer_name': self.customer_name,
            'customer_title': self.customer_title,
            'customer_phone_number': self.customer_phone_number,
            'customer_address': self.customer_address
        })

    @staticmethod
    def get(customer_id):
        response = customer_table.get_item(Key={'customer_id': customer_id})
        return response.get('Item')

    @classmethod
    def update(cls, customer_id, update_data):
        update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in update_data.keys()])
        expression_attribute_values = {f":{k}": v for k, v in update_data.items()}

        try:
            response = customer_table.update_item(
                Key={'customer_id': customer_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW"
            )
            if 'Attributes' in response:
                return response['Attributes']
            return None
        except ClientError as e:
            print(f"Error updating customer: {e}")
            return None

# from dynamodb_setup import dynamodb_resource

# customer_table = dynamodb_resource.Table('Customers')  # Ensure this matches the actual table name

# class Customers:
#     def __init__(self, customer_id, customer_name, customer_title=None, customer_phone_number=None, customer_address=None):
#         self.customer_id = str(customer_id)  # Ensure ID is a string
#         self.customer_name = customer_name
#         self.customer_title = customer_title
#         self.customer_phone_number = customer_phone_number
#         self.customer_address = customer_address

#     def save(self):
#         customer_table.put_item(Item={
#             'customer_id': self.customer_id,
#             'customer_name': self.customer_name,
#             'customer_title': self.customer_title,
#             'customer_phone_number': self.customer_phone_number,
#             'customer_address': self.customer_address
#         })

#     @staticmethod
#     def get(customer_id):
#         response = customer_table.get_item(Key={'customer_id': customer_id})
#         return response.get('Item')

#     @staticmethod
#     def update(customer_id, update_data):
#         customer = Customers.get(customer_id)
#         if not customer:
#             return None       
#         update_expression = "SET " + ", ".join([f"{k}=:{k}" for k in update_data.keys()])
#         expression_attribute_values = {f":{k}": v for k, v in update_data.items()}

#         customer_table.update_item(
#             Key={'customer_id': customer_id},
#             UpdateExpression=update_expression,
#             ExpressionAttributeValues=expression_attribute_values
#         )

#         return Customers.get(customer_id)
