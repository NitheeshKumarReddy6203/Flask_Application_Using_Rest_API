from flask import Blueprint, request, jsonify
from Models.product import Product
from Schemas.product_schema import ProductSchema

product_blueprint = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# POST: Create Product
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.json
    errors = product_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    try:
        product = Product(**data)
        product.save()
        return jsonify(data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# GET: Get Product by ID
@product_blueprint.route('/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.get(product_id)
        if not product:
            return jsonify({"message": "Product not found"}), 404
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT: Update Product
@product_blueprint.route('/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    # errors = product_schema.validate(data)
    # if errors:
        # return jsonify(errors), 400 
    try:
        updated_product = Product.update(product_id, data)
        if not updated_product:
            return jsonify({"message": "Product not found"}), 404
        return jsonify(updated_product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE: Delete Product
@product_blueprint.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        Product.delete(product_id)
        return jsonify({"message": "Product deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
