from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth import auth_models
from src.product import product_models

from .auth_data import ROLES, USERS
from .order_seeder import seed_order_items, seed_orders
from .product_data import CATEGORIES, PRODUCTS


async def seed_roles(session: AsyncSession):
    """Seed the roles table with default roles"""
    query = select(auth_models.Role.id)
    result = await session.execute(query)
    existing_role_ids = {role[0] for role in result.fetchall()}

    for role_data in ROLES:
        if role_data["id"] not in existing_role_ids:
            role = auth_models.Role(**role_data)
            session.add(role)

    await session.commit()


async def seed_users(session: AsyncSession):
    """Seed the users table with default users"""
    query = select(auth_models.User.id)
    result = await session.execute(query)
    existing_user_ids = {user[0] for user in result.fetchall()}

    for user_data in USERS:
        if user_data["id"] not in existing_user_ids:
            user = auth_models.User(**user_data)
            session.add(user)

    await session.commit()


async def seed_categories(session: AsyncSession):
    """Seed the categories table with default categories"""
    query = select(product_models.Category.id)
    result = await session.execute(query)
    existing_category_ids = {category[0] for category in result.fetchall()}

    for category_data in CATEGORIES:
        if category_data["id"] not in existing_category_ids:
            category = product_models.Category(**category_data)
            session.add(category)

    await session.commit()


async def seed_products(session: AsyncSession):
    """Seed the products table with default products"""
    query = select(product_models.Product.id)
    result = await session.execute(query)
    existing_product_ids = {product[0] for product in result.fetchall()}

    for product_data in PRODUCTS:
        if product_data["id"] not in existing_product_ids:
            product = product_models.Product(**product_data)
            session.add(product)

    await session.commit()


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
