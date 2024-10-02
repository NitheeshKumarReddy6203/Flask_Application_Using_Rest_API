import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
product_table = dynamodb.Table('Products')

class Product:
    def __init__(self, product_id, product_name, quantity_per_unit, unit_price):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_per_unit = quantity_per_unit
        self.unit_price = unit_price

    def save(self):
        try:
            response = product_table.put_item(
                Item={
                    'product_id': self.product_id,
                    'product_name': self.product_name,
                    'quantity_per_unit': self.quantity_per_unit,
                    'unit_price': self.unit_price
                }
            )
            return response
        except ClientError as e:
            print(f"Error saving product: {e}")
            raise

    @staticmethod
    def get(product_id):
        try:
            response = product_table.get_item(
                Key={'product_id': product_id}
            )
            item = response.get('Item')
            if item:
                return item
            else:
                return None
        except ClientError as e:
            print(f"Error retrieving product: {e}")
            raise

    @staticmethod
    def update(product_id, data):
        try:
            update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in data.keys()])
            expression_attribute_values = {f":{k}": v for k, v in data.items()}
            
            response = product_table.update_item(
                Key={'product_id': product_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW"
            )
            return response['Attributes']
        except ClientError as e:
            print(f"Error updating product: {e}")
            raise

    @staticmethod
    def delete(product_id):
        try:
            response = product_table.delete_item(
                Key={'product_id': product_id}
            )
            return response
        except ClientError as e:
            print(f"Error deleting product: {e}")
            raise
