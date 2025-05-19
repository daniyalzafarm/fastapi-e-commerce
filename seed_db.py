import asyncio

from seeders import seed_auth_data
from db.base import engine, get_db_session
from src.models import *  # This ensures all models are registered


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
