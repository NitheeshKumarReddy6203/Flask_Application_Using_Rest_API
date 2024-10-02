from marshmallow import ValidationError
from product_schema import ProductSchema
import json

data = {
    'product_id' : 123,
    'product_name' : 'Product',
    'quantity_per_Unit' : 10,
    'unit_price' : 25.8
}

schema = ProductSchema()
try:
    result = schema.load(data)
    print("\nPython Complex Data Type : \n", result)
    print("\n\n Type : ", type(result), "\n\n") 
except ValidationError as err:
    print("\nError Occured : ", err.messages)

if 'result' in locals():
    json_str = schema.dump(result)
    json_fin = json.dumps(json_str, indent=4)
    print(json_fin)
    print("\n\nType of : ", type(json_fin))
    









