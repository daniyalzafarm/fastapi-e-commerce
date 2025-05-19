from sqlalchemy.ext.asyncio import AsyncSession

from .auth_seeder import seed_roles, seed_users
from .order_seeder import seed_order_items, seed_orders
from .product_seeder import seed_categories, seed_products


async def seed_auth_data(session: AsyncSession):
    """Seed all auth-related data"""
    await seed_roles(session)
    await seed_users(session)


async def seed_product_data(session: AsyncSession):
    """Seed all product-related data"""
    await seed_categories(session)
    await seed_products(session)


async def seed_order_data(session: AsyncSession):
    """Seed all order-related data"""
    await seed_orders(session)
    await seed_order_items(session)
