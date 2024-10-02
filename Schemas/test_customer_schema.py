from marshmallow import ValidationError

# marshmallow : used to serialize ad deserialize the data
# Serilaize -> Converting : JSON FORMAT TO Python native data types
# DeSerialize -> Converting : python native datatypes to the JSOn formats or any other fromats

from customer_schema import CustomerSchema
data = {
    'customer_id' : 62003 , 
    'customer_name' : 'Nitheesh C', 
    'customer_title' : 'Intern',
    'customer_phone_number' : 9876543210,
    'customer_address' : 'Jain University, Kanaknapura Road'
}

schema = CustomerSchema()
try:
    result = schema.load(data)
    print(result)
except ValidationError as e:
    print("Validation Error ", e.messages)

json_data = schema.dump(result)
print(json_data)



