from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db_session

from . import product_schemas, product_services

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[product_schemas.ProductResponse])
async def get_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db_session),
):
    return await product_services.get_products(db, skip=skip, limit=limit)


@router.get("/{product_id}", response_model=product_schemas.ProductDetailResponse)
async def get_product_by_id(
    product_id: int,
    db: AsyncSession = Depends(get_db_session),
):
    product = await product_services.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=product_schemas.ProductResponse)
async def create_product(
    product: product_schemas.ProductCreate,
    db: AsyncSession = Depends(get_db_session),
):
    return await product_services.create_product(db, product)


@router.put("/{product_id}", response_model=product_schemas.ProductResponse)
async def update_product(
    product_id: int,
    product: product_schemas.ProductUpdate,
    db: AsyncSession = Depends(get_db_session),
):
    updated_product = await product_services.update_product(db, product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}")
async def delete_product(
    product_id: int,
    db: AsyncSession = Depends(get_db_session),
):
    success = await product_services.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


@router.get("/categories/", response_model=List[product_schemas.CategoryResponse])
async def get_categories(
    db: AsyncSession = Depends(get_db_session),
):
    return await product_services.get_categories(db)


@router.post("/categories/", response_model=product_schemas.CategoryResponse)
async def create_category(
    category: product_schemas.CategoryCreate,
    db: AsyncSession = Depends(get_db_session),
):
    return await product_services.create_category(db, category)
