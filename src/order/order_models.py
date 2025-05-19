from sqlalchemy import Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, UTC
from src.db.base import Base

class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"), nullable=False)
    ordered_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
    status: Mapped[str] = mapped_column(String(100), nullable=False)
    total_amount: Mapped[float] = mapped_column(Float, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    customer: Mapped["User"] = relationship(back_populates="orders")
    order_items: Mapped[list["OrderItem"]] = relationship(back_populates="order")

class OrderItem(Base):
    __tablename__ = "order_item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("order.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price_per_unit: Mapped[float] = mapped_column(Float, nullable=False)
    total_price: Mapped[float] = mapped_column(Float, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    order: Mapped["Order"] = relationship(back_populates="order_items")
    product: Mapped["Product"] = relationship()
