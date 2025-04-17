from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Product:
    """Represents a grocery product with its attributes."""
    id: int               # Unique product identifier
    name: str             # Product name (must be unique)
    price_per_unit: float # Price per unit (must be positive)
    unit: str             # Unit of measurement (e.g., kg, liter)

@dataclass
class OrderItem:
    """Represents an item within an order."""
    product_id: int  # References Product.id
    quantity: int    # Must be a positive integer

@dataclass
class Order:
    """Represents a customer order with calculated total."""
    order_id: int               # Unique order identifier
    customer_name: str          # Name of the customer
    items: List[OrderItem]      # List of ordered items
    total_amount: float         # Sum of (price * quantity) for all items