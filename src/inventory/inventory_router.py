from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db_session

from . import inventory_schemas, inventory_services

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("/", response_model=List[inventory_schemas.InventoryResponse])
async def list_inventory(
    db: AsyncSession = Depends(get_db_session),
):
    """List current inventory status of all products."""
    return await inventory_services.get_all_inventory(db)


@router.get("/{product_id}", response_model=List[inventory_schemas.InventoryResponse])
async def get_product_inventory_route(
    product_id: int,
    db: AsyncSession = Depends(get_db_session),
):
    """Get inventory for a specific product."""
    inventory = await inventory_services.get_product_inventory(db, product_id)
    if not inventory:
        raise HTTPException(status_code=404, detail="Product inventory not found")
    return inventory


@router.put("/{product_id}", response_model=inventory_schemas.InventoryResponse)
async def update_inventory_route(
    product_id: int,
    warehouse_id: int = Query(..., description="Warehouse ID"),
    update_data: inventory_schemas.InventoryUpdate = None,
    db: AsyncSession = Depends(get_db_session),
):
    """Update inventory for a product."""
    try:
        return await inventory_services.update_inventory(
            db, product_id, warehouse_id, update_data
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/low-stock", response_model=List[inventory_schemas.LowStockProduct])
async def get_low_stock_products_route(
    threshold: int = Query(10, description="Minimum quantity threshold"),
    db: AsyncSession = Depends(get_db_session),
):
    """Get products with low stock levels."""
    return await inventory_services.get_low_stock_products(db, threshold)


@router.get(
    "/history/{product_id}", response_model=List[inventory_schemas.InventoryLogResponse]
)
async def get_inventory_history_route(
    product_id: int,
    warehouse_id: Optional[int] = Query(None, description="Filter by warehouse ID"),
    db: AsyncSession = Depends(get_db_session),
):
    """Get inventory change history for a product."""
    history = await inventory_services.get_inventory_history(
        db, product_id, warehouse_id
    )
    if not history:
        raise HTTPException(status_code=404, detail="No inventory history found")
    return history
