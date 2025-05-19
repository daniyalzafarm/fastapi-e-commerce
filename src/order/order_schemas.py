from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    price_per_unit: float = Field(gt=0)
    total_price: float = Field(gt=0)


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int
    order_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class OrderBase(BaseModel):
    customer_id: int
    status: str
    total_amount: float = Field(gt=0)


class OrderCreate(OrderBase):
    order_items: List[OrderItemCreate]


class OrderResponse(OrderBase):
    id: int
    ordered_at: datetime
    created_at: datetime
    updated_at: datetime
    order_items: List[OrderItemResponse]

    class Config:
        from_attributes = True


class OrderListResponse(BaseModel):
    items: List[OrderResponse]
    total: int
    page: int
    size: int
    pages: int


class OrderFilter(BaseModel):
    status: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class DailyOrderAnalytics(BaseModel):
    date: datetime
    total_orders: int
    total_revenue: float


class ProductOrderAnalytics(BaseModel):
    product_id: int
    product_name: str
    total_quantity_sold: int
    total_revenue: float


class CategoryOrderAnalytics(BaseModel):
    category_id: int
    category_name: str
    total_orders: int
    total_revenue: float
