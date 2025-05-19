from src.auth import Role, User
from src.order import Order, OrderItem
from src.product import Product, Category, ProductImage
from src.inventory import Inventory, InventoryLog
from src.warehouse import Warehouse

# This file ensures all models are imported and registered with SQLAlchemy
__all__ = [
    # Auth models
    "Role", "User",
    # Order models
    "Order", "OrderItem",
    # Product models
    "Product", "Category", "ProductImage",
    # Inventory models
    "Inventory", "InventoryLog",
    # Warehouse models
    "Warehouse"
]
