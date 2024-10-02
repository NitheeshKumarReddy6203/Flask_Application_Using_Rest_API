import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
order_table = dynamodb.Table('Orders')

class Order:
    def __init__(self, order_id, customer_id, order_date, shipped_date=None, delivery_fee=None):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.shipped_date = shipped_date
        self.delivery_fee = delivery_fee

    def save(self):
        try:
            response = order_table.put_item(
                Item={
                    'order_id': self.order_id,
                    'customer_id': self.customer_id,
                    'order_date': str(self.order_date),  # Convert date to string if needed
                    'shipped_date': str(self.shipped_date) if self.shipped_date else None,  # Convert date to string if needed
                    'delivery_fee': self.delivery_fee
                }
            )
            return response
        except ClientError as e:
            print(f"Error saving order: {e}")
            raise

    @staticmethod
    def get(order_id):
        try:
            response = order_table.get_item(
                Key={'order_id': order_id}
            )
            item = response.get('Item')
            if item:
                return item
            else:
                return None
        except ClientError as e:
            print(f"Error retrieving order: {e}")
            raise

    @staticmethod
    def update(order_id, data):
        try:
            update_expression = "SET " + ", ".join([f"{k} = :{k}" for k in data.keys()])
            expression_attribute_values = {f":{k}": v for k, v in data.items()}
            
            response = order_table.update_item(
                Key={'order_id': order_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW"
            )
            return response['Attributes']
        except ClientError as e:
            print(f"Error updating order: {e}")
            raise
