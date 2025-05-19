import asyncio
from src.db.base import get_db_session, engine
from seeders import seed_auth_data

# Import all models to ensure they are registered
from src.auth import User, Role
from src.order import Order, OrderItem
from src.product import Product, Category, ProductImage
from src.inventory import Inventory, InventoryLog
from src.warehouse import Warehouse

async def seed_database():
    """Seed the database with initial data"""
    try:
        async for session in get_db_session():
            print("=== Starting database seeding ===")
            await seed_auth_data(session)
            print("=== Database seeding completed ===")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(seed_database())
