from datetime import datetime
from typing import List

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.order.order_models import Order, OrderItem
from src.product.product_models import Category, Product

from . import order_schemas


async def create_order(
    session: AsyncSession, order_data: order_schemas.OrderCreate
) -> order_schemas.OrderResponse:
    order_dict = order_data.model_dump(exclude={"order_items"})
    order_items = order_data.order_items

    order = Order(**order_dict)
    session.add(order)
    await session.flush()

    for item in order_items:
        item["order_id"] = order.id
        order_item = OrderItem(**item)
        session.add(order_item)

    await session.commit()
    await session.refresh(order)
    return order_schemas.OrderResponse.model_validate(order)


async def get_order_by_id(
    session: AsyncSession,
    order_id: int,
) -> order_schemas.OrderResponse:
    """Get a specific order by ID"""
    query = (
        select(Order)
        .options(selectinload(Order.order_items))
        .where(Order.id == order_id)
    )
    result = await session.execute(query)
    order = result.scalar_one_or_none()

    if not order:
        raise ValueError(f"Order with ID {order_id} not found")

    return order_schemas.OrderResponse.model_validate(order)


async def get_user_orders(
    session: AsyncSession,
    user_id: int,
    page: int,
    size: int,
    filters: order_schemas.OrderFilter,
) -> order_schemas.OrderListResponse:
    """Get orders for a specific user with pagination and filters"""
    query = select(Order).where(Order.customer_id == user_id)

    if filters.status:
        query = query.where(Order.status == filters.status)
    if filters.start_date:
        query = query.where(Order.ordered_at >= filters.start_date)
    if filters.end_date:
        query = query.where(Order.ordered_at <= filters.end_date)

    count_query = select(func.count()).select_from(query.subquery())
    total = await session.scalar(count_query)

    total_pages = (total + size - 1) // size if total > 0 else 1

    query = (
        query.options(selectinload(Order.order_items))
        .order_by(Order.ordered_at.desc())
        .offset((page - 1) * size)
        .limit(size)
    )

    result = await session.execute(query)
    orders = result.scalars().all()

    return order_schemas.OrderListResponse(
        total=total,
        page=page,
        size=size,
        pages=total_pages,
        items=[order_schemas.OrderResponse.model_validate(order) for order in orders],
    )


async def get_daily_analytics(
    session: AsyncSession, start_date: datetime, end_date: datetime
) -> List[order_schemas.DailyOrderAnalytics]:
    query = (
        select(
            func.date(Order.ordered_at).label("date"),
            func.count(Order.id).label("total_orders"),
            func.sum(Order.total_amount).label("total_revenue"),
        )
        .where(Order.ordered_at.between(start_date, end_date))
        .group_by(func.date(Order.ordered_at))
        .order_by(func.date(Order.ordered_at))
    )
    result = await session.execute(query)
    analytics = result.mappings().all()
    return [order_schemas.DailyOrderAnalytics(**item) for item in analytics]


async def get_product_analytics(
    session: AsyncSession,
    start_date: datetime,
    end_date: datetime,
    product_id: int | None = None,
) -> List[order_schemas.ProductOrderAnalytics]:
    query = (
        select(
            OrderItem.product_id,
            Product.name.label("product_name"),
            func.sum(OrderItem.quantity).label("total_quantity_sold"),
            func.sum(OrderItem.total_price).label("total_revenue"),
        )
        .join(Order)
        .join(Product)
        .where(Order.ordered_at.between(start_date, end_date))
    )

    if product_id is not None:
        query = query.where(OrderItem.product_id == product_id)

    query = query.group_by(OrderItem.product_id, Product.name).order_by(
        func.sum(OrderItem.total_price).desc()
    )

    result = await session.execute(query)
    analytics = result.mappings().all()
    return [order_schemas.ProductOrderAnalytics(**item) for item in analytics]


async def get_category_analytics(
    session: AsyncSession,
    start_date: datetime,
    end_date: datetime,
    category_id: int | None = None,
) -> List[order_schemas.CategoryOrderAnalytics]:
    query = (
        select(
            Product.category_id,
            Category.name.label("category_name"),
            func.count(Order.id).label("total_orders"),
            func.sum(OrderItem.total_price).label("total_revenue"),
        )
        .select_from(OrderItem)
        .join(Order, OrderItem.order_id == Order.id)
        .join(Product, OrderItem.product_id == Product.id)
        .join(Category, Product.category_id == Category.id)
        .where(Order.ordered_at.between(start_date, end_date))
    )

    if category_id is not None:
        query = query.where(Product.category_id == category_id)

    query = query.group_by(Product.category_id, Category.name).order_by(
        func.sum(OrderItem.total_price).desc()
    )

    result = await session.execute(query)
    analytics = result.mappings().all()
    return [order_schemas.CategoryOrderAnalytics(**item) for item in analytics]
