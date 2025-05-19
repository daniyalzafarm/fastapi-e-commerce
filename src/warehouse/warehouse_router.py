from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db_session

from . import warehouse_schemas, warehouse_services

router = APIRouter(prefix="/warehouses", tags=["warehouses"])


@router.get("/", response_model=List[warehouse_schemas.WarehouseResponse])
async def get_warehouses(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db_session),
):
    return await warehouse_services.get_warehouses(db, skip=skip, limit=limit)


@router.get("/{warehouse_id}", response_model=warehouse_schemas.WarehouseResponse)
async def get_warehouse_by_id(
    warehouse_id: int,
    db: AsyncSession = Depends(get_db_session),
):
    warehouse = await warehouse_services.get_warehouse(db, warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return warehouse


@router.post("/", response_model=warehouse_schemas.WarehouseResponse)
async def create_warehouse(
    warehouse: warehouse_schemas.WarehouseCreate,
    db: AsyncSession = Depends(get_db_session),
):
    return await warehouse_services.create_warehouse(db, warehouse)
