from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.inventory.inventory_models import Inventory, InventoryLog
from src.inventory.inventory_schemas import InventoryCreate, InventoryUpdate


async def get_all_inventory(db: AsyncSession) -> List[Inventory]:
    """Get all inventory records."""
    result = await db.execute(select(Inventory))
    return result.scalars().all()


async def get_product_inventory(db: AsyncSession, product_id: int) -> List[Inventory]:
    """Get inventory records for a specific product."""
    result = await db.execute(
        select(Inventory).where(Inventory.product_id == product_id)
    )
    return result.scalars().all()


async def update_inventory(
    db: AsyncSession, product_id: int, warehouse_id: int, update_data: InventoryUpdate
) -> Inventory:
    """Update inventory for a product and create inventory log."""
    # Get current inventory
    result = await db.execute(
        select(Inventory).where(
            Inventory.product_id == product_id,
            Inventory.warehouse_id == warehouse_id,
        )
    )
    inventory = result.scalar_one_or_none()

    if not inventory:
        # Create new inventory record
        inventory = Inventory(
            product_id=product_id,
            warehouse_id=warehouse_id,
            quantity=update_data.quantity,
        )
        db.add(inventory)
    else:
        # Update existing inventory
        previous_quantity = inventory.quantity
        inventory.quantity = update_data.quantity

        # Create inventory log
        inventory_log = InventoryLog(
            product_id=product_id,
            warehouse_id=warehouse_id,
            quantity_change=update_data.quantity - previous_quantity,
            previous_quantity=previous_quantity,
            new_quantity=update_data.quantity,
            reason=update_data.reason,
        )
        db.add(inventory_log)

    await db.commit()
    await db.refresh(inventory)
    return inventory


async def get_low_stock_products(db: AsyncSession, threshold: int = 10) -> List[dict]:
    """Get products with quantity below threshold."""
    query = """
        SELECT 
            i.product_id,
            p.name as product_name,
            i.quantity as current_quantity,
            i.warehouse_id,
            w.name as warehouse_name
        FROM inventory i
        JOIN product p ON i.product_id = p.id
        JOIN warehouse w ON i.warehouse_id = w.id
        WHERE i.quantity < :threshold
        ORDER BY i.quantity ASC
    """
    result = await db.execute(query, {"threshold": threshold})
    return result.mappings().all()


async def get_inventory_history(
    db: AsyncSession, product_id: int, warehouse_id: Optional[int] = None
) -> List[InventoryLog]:
    """Get inventory change history for a product."""
    query = select(InventoryLog).where(InventoryLog.product_id == product_id)
    if warehouse_id:
        query = query.where(InventoryLog.warehouse_id == warehouse_id)
    query = query.order_by(InventoryLog.created_at.desc())

    result = await db.execute(query)
    return result.scalars().all()
