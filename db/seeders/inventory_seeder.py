from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.inventory import inventory_models

from .inventory_data import INVENTORY, INVENTORY_LOGS


async def seed_inventory(session: AsyncSession):
    """Seed the inventory table with default inventory data"""
    query = select(inventory_models.Inventory)
    result = await session.execute(query)
    existing_inventory = {
        (inv.product_id, inv.warehouse_id) for inv in result.scalars().all()
    }

    for inventory_data in INVENTORY:
        key = (inventory_data["product_id"], inventory_data["warehouse_id"])
        if key not in existing_inventory:
            inventory = inventory_models.Inventory(**inventory_data)
            session.add(inventory)

    await session.commit()


async def seed_inventory_logs(session: AsyncSession):
    """Seed the inventory_logs table with default inventory logs"""
    query = select(inventory_models.InventoryLog.id)
    result = await session.execute(query)
    existing_log_ids = {log[0] for log in result.fetchall()}

    for log_data in INVENTORY_LOGS:
        if log_data["id"] not in existing_log_ids:
            log = inventory_models.InventoryLog(**log_data)
            session.add(log)

    await session.commit()
