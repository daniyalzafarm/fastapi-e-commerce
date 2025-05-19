from datetime import datetime, UTC
from typing import Optional
from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.base import Base

class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"), nullable=False)
    warehouse_id: Mapped[int] = mapped_column(Integer, ForeignKey("warehouse.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    product: Mapped["Product"] = relationship(back_populates="inventories")
    warehouse: Mapped["Warehouse"] = relationship(back_populates="inventories")

class InventoryLog(Base):
    __tablename__ = "inventory_log"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"), nullable=False)
    warehouse_id: Mapped[int] = mapped_column(Integer, ForeignKey("warehouse.id"), nullable=False)

    quantity_change: Mapped[int] = mapped_column(Integer, nullable=False)
    previous_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    new_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    reason: Mapped[Optional[str]] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))

    product: Mapped["Product"] = relationship()
    warehouse: Mapped["Warehouse"] = relationship(back_populates="inventory_logs")