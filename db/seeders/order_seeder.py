from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.order.order_models import Order, OrderItem

from .order_data import ORDER_ITEMS, ORDERS


async def seed_orders(session: AsyncSession):
    """Seed the orders table with default orders"""
    query = select(Order.id)
    result = await session.execute(query)
    existing_order_ids = {order[0] for order in result.fetchall()}

    for order_data in ORDERS:
        if order_data["id"] not in existing_order_ids:
            order = Order(**order_data)
            session.add(order)

    await session.commit()


async def seed_order_items(session: AsyncSession):
    """Seed the order items table with default order items"""
    query = select(OrderItem.id)
    result = await session.execute(query)
    existing_order_item_ids = {item[0] for item in result.fetchall()}

    for item_data in ORDER_ITEMS:
        if item_data["id"] not in existing_order_item_ids:
            order_item = OrderItem(**item_data)
            session.add(order_item)

    await session.commit()
