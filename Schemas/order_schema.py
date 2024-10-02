from marshmallow import fields, Schema

class OrderSchema(Schema):
    order_id = fields.Str(required=True)  # String for order_id
    customer_id = fields.Str(required=True)  # String for customer_id
    order_date = fields.Date(required=True)  # Date for order_date
    shipped_date = fields.Date()  # Optional date
    delivery_fee = fields.Int(required=True)  # Integer for delivery_fee
