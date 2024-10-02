from flask import Blueprint, request, jsonify
from Models.order import Order
from Schemas.order_schema import OrderSchema

order_blueprint = Blueprint('orders', __name__)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@order_blueprint.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    errors = order_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    try:
        order = Order(**data)
        order.save()
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@order_blueprint.route('/orders/<string:order_id>', methods=['GET'])
def get_order(order_id):
    try:
        order = Order.get(order_id)
        if not order:
            return jsonify({"message": "Order not found"}), 404
        return jsonify(order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@order_blueprint.route('/orders/<string:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    # errors = order_schema.validate(data)
    # if errors:
        # return jsonify(errors), 400
    try:
        updated_order = Order.update(order_id, data)
        if not updated_order:
            return jsonify({"message": "Order not found"}), 404
        return jsonify(updated_order), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
