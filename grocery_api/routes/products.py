from flask import Blueprint, request, jsonify
from services.product_service import add_product, get_all_products
from utils.validators import validate_product
from models import Product

# Create Blueprint for product-related routes
bp = Blueprint('products', __name__)

@bp.route('/', methods=['POST'])
def create_product():
    """Endpoint to create a new product.
    
    Request JSON:
        {
            "name": "Product name",
            "price_per_unit": 10.99,
            "unit": "kg"
        }
    
    Returns:
        201 Created: On successful creation
        400 Bad Request: If validation fails
    """
    data = request.get_json()
    try:
        validate_product(data)
        product = add_product(**data)
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price_per_unit": product.price_per_unit,
            "unit": product.unit
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/', methods=['GET'])
def list_products():
    """Endpoint to list all products.
    
    Returns:
        200 OK: With list of products
    """
    products = get_all_products()
    return jsonify([{
        "id": p.id,
        "name": p.name,
        "price_per_unit": p.price_per_unit,
        "unit": p.unit
    } for p in products]), 200