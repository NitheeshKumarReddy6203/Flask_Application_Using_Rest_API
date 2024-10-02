

# from marshmallow import Schema, fields, validate

# class CustomerSchema(Schema):
#     customer_id = fields.Str(required=True, validate=validate.Length(max=5))
#     customer_name = fields.Str(required=True, validate=validate.Length(max=20))
#     customer_title = fields.Str(validate=validate.Length(max=20))
#     customer_phone_number = fields.Int(validate=validate.Range(min=1000000000, max=9999999999))
#     customer_address = fields.Str(validate=validate.Length(max=50))
# #

from marshmallow import Schema, fields, validate

class CustomerSchema(Schema):
    customer_id = fields.Str(required=True, validate=validate.Length(max=5))
    customer_name = fields.Str(required=True, validate=validate.Length(max=20))
    customer_title = fields.Str(validate=validate.Length(max=20))
    customer_phone_number = fields.Int(validate=validate.Range(min=1000000000, max=9999999999))
    customer_address = fields.Str(validate=validate.Length(max=50))
