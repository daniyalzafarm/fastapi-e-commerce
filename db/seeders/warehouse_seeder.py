from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.warehouse import warehouse_models

from .warehouse_data import WAREHOUSES


async def seed_warehouses(session: AsyncSession):
    """Seed the warehouses table with default warehouses"""
    query = select(warehouse_models.Warehouse.id)
    result = await session.execute(query)
    existing_warehouse_ids = {warehouse[0] for warehouse in result.fetchall()}

    for warehouse_data in WAREHOUSES:
        if warehouse_data["id"] not in existing_warehouse_ids:
            warehouse = warehouse_models.Warehouse(**warehouse_data)
            session.add(warehouse)

    await session.commit()
