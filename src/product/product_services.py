from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.product.product_models import Category, Product, ProductImage
from src.product.product_schemas import (
    CategoryCreate,
    CategoryUpdate,
    ProductCreate,
    ProductUpdate,
)


async def get_products(
    db: AsyncSession, skip: int = 0, limit: int = 10
) -> List[Product]:
    query = (
        select(Product)
        .options(selectinload(Product.category))
        .offset(skip)
        .limit(limit)
    )
    result = await db.execute(query)
    return result.scalars().all()


async def get_product(db: AsyncSession, product_id: int) -> Optional[Product]:
    query = (
        select(Product)
        .options(selectinload(Product.category), selectinload(Product.images))
        .where(Product.id == product_id)
    )
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def create_product(db: AsyncSession, product: ProductCreate) -> Product:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def update_product(
    db: AsyncSession, product_id: int, product: ProductUpdate
) -> Optional[Product]:
    db_product = await get_product(db, product_id)
    if not db_product:
        return None

    update_data = product.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_product, field, value)

    await db.commit()
    await db.refresh(db_product)
    return db_product


async def delete_product(db: AsyncSession, product_id: int) -> bool:
    db_product = await get_product(db, product_id)
    if not db_product:
        return False

    await db.delete(db_product)
    await db.commit()
    return True


async def get_categories(db: AsyncSession) -> List[Category]:
    query = select(Category)
    result = await db.execute(query)
    return result.scalars().all()


async def create_category(db: AsyncSession, category: CategoryCreate) -> Category:
    db_category = Category(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category


async def update_category(
    db: AsyncSession, category_id: int, category: CategoryUpdate
) -> Optional[Category]:
    query = select(Category).where(Category.id == category_id)
    result = await db.execute(query)
    db_category = result.scalar_one_or_none()

    if not db_category:
        return None

    update_data = category.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)

    await db.commit()
    await db.refresh(db_category)
    return db_category
