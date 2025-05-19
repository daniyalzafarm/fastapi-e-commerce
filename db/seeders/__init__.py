from sqlalchemy.ext.asyncio import AsyncSession

from .auth_seeder import seed_roles, seed_users
from .inventory_seeder import seed_inventory, seed_inventory_logs
from .order_seeder import seed_order_items, seed_orders
from .product_seeder import seed_categories, seed_products
from .warehouse_seeder import seed_warehouses


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


async def seed_warehouse_data(session: AsyncSession):
    """Seed all warehouse-related data"""
    await seed_warehouses(session)


async def seed_inventory_data(session: AsyncSession):
    """Seed all inventory-related data"""
    await seed_inventory(session)
    await seed_inventory_logs(session)
