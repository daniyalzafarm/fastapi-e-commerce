import asyncio

from src.models import *  # This ensures all models are registered

from .base import engine, get_db_session
from .seeders import (
    seed_auth_data,
    seed_inventory_data,
    seed_order_data,
    seed_product_data,
    seed_warehouse_data,
)


async def seed_database():
    """Seed the database with initial data"""
    try:
        async for session in get_db_session():
            print("=== Starting database seeding ===")
            await seed_auth_data(session)
            await seed_product_data(session)
            await seed_order_data(session)
            await seed_warehouse_data(session)
            await seed_inventory_data(session)
            print("=== Database seeding completed ===")
    finally:
        await engine.dispose()


if __name__ == "__main__":
    asyncio.run(seed_database())
