from models import Product

# In-memory database for products (replace with real DB in production)
products_db = []
next_id = 1  # Auto-incrementing ID counter

def add_product(name: str, price_per_unit: float, unit: str) -> Product:
    """Adds a new product to the database.
    
    Args:
        name: Unique product name
        price_per_unit: Positive price value
        unit: Unit of measurement
    
    Returns:
        The created Product object
    """
    global next_id
    product = Product(id=next_id, name=name, price_per_unit=price_per_unit, unit=unit)
    products_db.append(product)
    next_id += 1
    return product

def get_all_products() -> list[Product]:
    """Retrieves all products from the database.
    
    Returns:
        List of Product objects
    """
    return products_db

def get_product_by_id(product_id: int) -> Product:
    """Finds a product by its ID.
    
    Args:
        product_id: The ID to search for
    
    Returns:
        Product object if found, None otherwise
    """
    return next((p for p in products_db if p.id == product_id), None)