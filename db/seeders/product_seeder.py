from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.product import product_models

from .product_data import CATEGORIES, PRODUCTS


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
