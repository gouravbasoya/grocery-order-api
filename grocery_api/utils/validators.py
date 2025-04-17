from services.product_service import get_all_products

def validate_product(data: dict):
    """Validates product data before creation.
    
    Args:
        data: Dictionary containing product attributes
    
    Raises:
        ValueError: If any validation fails
    """
    if not data.get("name") or not isinstance(data["name"], str):
        raise ValueError("Name must be a non-empty string")
    
    # Check for unique product name
    if any(p.name == data["name"] for p in get_all_products()):
        raise ValueError("Product name must be unique")
    
    # Validate price
    if not isinstance(data.get("price_per_unit"), (int, float)) or data["price_per_unit"] <= 0:
        raise ValueError("Price must be a positive number")

def validate_order(data: dict):
    """Validates order data before creation.
    
    Args:
        data: Dictionary containing order details
    
    Raises:
        ValueError: If any validation fails
    """
    if not data.get("customer_name") or not isinstance(data["customer_name"], str):
        raise ValueError("Customer name must be a non-empty string")
    
    # Validate items list
    if not isinstance(data.get("items"), list) or len(data["items"]) == 0:
        raise ValueError("Items must be a non-empty list")
    
    # Validate each item's quantity
    for item in data["items"]:
        if not isinstance(item.get("quantity"), int) or item["quantity"] <= 0:
            raise ValueError("Quantity must be a positive integer")