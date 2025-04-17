from models import Order, OrderItem
from services.product_service import get_product_by_id

# In-memory database for orders
orders_db = []
next_id = 1  # Auto-incrementing ID counter

def place_order(customer_name: str, items: list[dict]) -> Order:
    """Creates a new order with calculated total amount.
    
    Args:
        customer_name: Name of the ordering customer
        items: List of items with product_id and quantity
    
    Returns:
        The created Order object
    
    Raises:
        ValueError: If any product ID is invalid
    """
    global next_id
    order_items = []
    total = 0.0

    # Process each item in the order
    for item in items:
        product = get_product_by_id(item["product_id"])
        if not product:
            raise ValueError(f"Invalid product ID: {item['product_id']}")
        
        # Calculate item subtotal and add to order
        total += product.price_per_unit * item["quantity"]
        order_items.append(OrderItem(**item))

    # Create and store the order
    order = Order(
        order_id=next_id,
        customer_name=customer_name,
        items=order_items,
        total_amount=total
    )
    orders_db.append(order)
    next_id += 1
    return order

def get_all_orders() -> list[Order]:
    """Retrieves all orders from the database.
    
    Returns:
        List of Order objects
    """
    return orders_db