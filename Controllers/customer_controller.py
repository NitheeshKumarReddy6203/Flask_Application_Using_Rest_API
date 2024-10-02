
from flask import Blueprint, request, jsonify
from Models.customer import Customers
from Schemas.customer_schema import CustomerSchema
customer_blueprint = Blueprint('customers', __name__)
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

@customer_blueprint.route('/customers', methods=['POST'])
def create_customer():
    data = request.json
    errors = customer_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    customer = Customers(**data)
    customer.save()
    result = customer_schema.dump(customer)
    return jsonify(result), 201 

@customer_blueprint.route('/customers/<string:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customers.get(customer_id)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404
    return jsonify(customer), 200

@customer_blueprint.route('/customers/<string:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.json

    if 'customer_id' not in data:
        data['customer_id'] = customer_id

    # errors = customer_schema.validate(data)
    # if errors:
        # return jsonify(errors), 400

    updated_customer = Customers.update(customer_id, data)
    if not updated_customer:
        return jsonify({"message": "Customer not found"}), 404

    result = customer_schema.dump(updated_customer)
    return jsonify(result), 200

