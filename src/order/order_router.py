from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_db_session

from . import order_schemas, order_services

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/user/{user_id}", response_model=order_schemas.OrderListResponse)
async def list_user_orders(
    user_id: int,
    page: int = Query(1, ge=1, description="Page number, starting from 1"),
    size: int = Query(10, ge=1, le=100, description="Number of items per page"),
    status: str | None = Query(None, description="Filter by order status"),
    start_date: datetime | None = Query(
        None, description="Filter orders from this date (inclusive)"
    ),
    end_date: datetime | None = Query(
        None, description="Filter orders until this date (inclusive)"
    ),
    session: AsyncSession = Depends(get_db_session),
):
    filters = order_schemas.OrderFilter(
        status=status,
        start_date=start_date,
        end_date=end_date,
    )
    return await order_services.get_user_orders(session, user_id, page, size, filters)


@router.get("/analytics", response_model=List[order_schemas.DailyOrderAnalytics])
async def get_daily_analytics_endpoint(
    start_date: datetime = Query(
        ...,
        description="Start date for analytics (inclusive)",
        example="2024-01-01T00:00:00Z",
    ),
    end_date: datetime = Query(
        ...,
        description="End date for analytics (inclusive)",
        example="2024-01-31T23:59:59Z",
    ),
    session: AsyncSession = Depends(get_db_session),
):
    """
    Get daily order analytics between two dates.

    Returns:
    - date: The date of the analytics
    - total_orders: Number of orders on that date
    - total_revenue: Total revenue for that date
    """
    return await order_services.get_daily_analytics(session, start_date, end_date)


@router.get(
    "/analytics/by-product", response_model=List[order_schemas.ProductOrderAnalytics]
)
async def get_product_analytics_endpoint(
    start_date: datetime = Query(
        ...,
        description="Start date for analytics (inclusive)",
        example="2024-01-01T00:00:00Z",
    ),
    end_date: datetime = Query(
        ...,
        description="End date for analytics (inclusive)",
        example="2024-01-31T23:59:59Z",
    ),
    product_id: int | None = Query(
        None,
        description="Optional: Filter analytics for a specific product",
        example=1,
    ),
    session: AsyncSession = Depends(get_db_session),
):
    """
    Get product-wise order analytics between two dates.

    Returns:
    - product_id: ID of the product
    - product_name: Name of the product
    - total_quantity_sold: Total quantity sold
    - total_revenue: Total revenue from this product
    """
    return await order_services.get_product_analytics(
        session, start_date, end_date, product_id
    )


@router.get(
    "/analytics/by-category", response_model=List[order_schemas.CategoryOrderAnalytics]
)
async def get_category_analytics_endpoint(
    start_date: datetime = Query(
        ...,
        description="Start date for analytics (inclusive)",
        example="2024-01-01T00:00:00Z",
    ),
    end_date: datetime = Query(
        ...,
        description="End date for analytics (inclusive)",
        example="2024-01-31T23:59:59Z",
    ),
    category_id: int | None = Query(
        None,
        description="Optional: Filter analytics for a specific category",
        example=1,
    ),
    session: AsyncSession = Depends(get_db_session),
):
    """
    Get category-wise order analytics between two dates.

    Returns:
    - category_id: ID of the category
    - category_name: Name of the category
    - total_orders: Number of orders in this category
    - total_revenue: Total revenue from this category
    """
    return await order_services.get_category_analytics(
        session, start_date, end_date, category_id
    )


@router.get("/{order_id}", response_model=order_schemas.OrderResponse)
async def get_order(
    order_id: int,
    session: AsyncSession = Depends(get_db_session),
):
    return await order_services.get_order_by_id(session, order_id)


@router.post("/", response_model=order_schemas.OrderResponse)
async def create_order_endpoint(
    order_data: order_schemas.OrderCreate,
    session: AsyncSession = Depends(get_db_session),
):
    return await order_services.create_order(session, order_data)
