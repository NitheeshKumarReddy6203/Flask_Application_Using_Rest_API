from marshmallow import ValidationError
from product_schema import ProductSchema
import json
data = {
    'order_id' : 123,
    'customer_id': 62003,
    'order_date' : '2024-08-30',
    'shipped_date' : '2024-09-09',
    'delivery_fee' : 34
}
schema = ProductSchema()
try:
    result = schema.load(data)
    print("\nPython Complex Data Type : \n", result)
    print("\n\n Type : ", type(result), "\n\n")
except ValidationError as err:
    print("\nError Occuured : ", err.messages)

json_format = schema.dump(result)
print("\nConverted to JSON (Assumption) : \n", json_format)
print("\n\n Type : ", type(json_format), "\n\n")

json_string = json.dumps(json_format)
print("\nConverted to JSON Format : \n", json_string)
print("\n\n Type : ", type(json_string), "\n\n")
