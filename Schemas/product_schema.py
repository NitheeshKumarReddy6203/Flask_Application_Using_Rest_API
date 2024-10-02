from marshmallow import fields, validate, Schema

class ProductSchema(Schema):
    product_id = fields.Int(required=True)
    product_name = fields.Str(required=True, validate=lambda s: len(s) <= 20)
    quantity_per_unit = fields.Int()
    unit_price = fields.Float()
