from flask import Blueprint, request, jsonify
from services.order_service import place_order, get_all_orders
from services.product_service import get_all_products
from utils.validators import validate_order
from models import Order

# Create Blueprint for order-related routes
bp = Blueprint('orders', __name__)

@bp.route('/', methods=['POST'])
def create_order():
    """Endpoint to place a new order.
    
    Request JSON:
        {
            "customer_name": "John Doe",
            "items": [
                {"product_id": 1, "quantity": 2}
            ]
        }
    
    Returns:
        201 Created: On successful order placement
        400 Bad Request: If validation fails
    """
    data = request.get_json()
    try:
        validate_order(data)
        order = place_order(**data)
        return jsonify({
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "items": [{
                "product_id": item.product_id,
                "quantity": item.quantity
            } for item in order.items],
            "total_amount": order.total_amount
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@bp.route('/', methods=['GET'])
def list_orders():
    """Endpoint to list all orders with detailed item info.
    
    Returns:
        200 OK: With list of orders including calculated totals
    """
    orders = get_all_orders()
    all_products = get_all_products()
    
    return jsonify([{
        "order_id": o.order_id,
        "customer_name": o.customer_name,
        "items": [{
            "product_id": item.product_id,
            "product_name": next(
                p.name for p in all_products 
                if p.id == item.product_id
            ),
            "quantity": item.quantity,
            "price": item.quantity * next(
                p.price_per_unit for p in all_products 
                if p.id == item.product_id
            )
        } for item in o.items],
        "total_amount": o.total_amount
    } for o in orders]), 200