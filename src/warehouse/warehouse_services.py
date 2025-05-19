from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import warehouse_models, warehouse_schemas


async def get_warehouses(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> List[warehouse_models.Warehouse]:
    query = select(warehouse_models.Warehouse).offset(skip).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


async def get_warehouse(
    db: AsyncSession,
    warehouse_id: int,
) -> Optional[warehouse_models.Warehouse]:
    query = select(warehouse_models.Warehouse).where(
        warehouse_models.Warehouse.id == warehouse_id
    )
    result = await db.execute(query)
    return result.scalar_one_or_none()


async def create_warehouse(
    db: AsyncSession,
    warehouse: warehouse_schemas.WarehouseCreate,
) -> warehouse_models.Warehouse:
    db_warehouse = warehouse_models.Warehouse(**warehouse.model_dump())
    db.add(db_warehouse)
    await db.commit()
    await db.refresh(db_warehouse)
    return db_warehouse
