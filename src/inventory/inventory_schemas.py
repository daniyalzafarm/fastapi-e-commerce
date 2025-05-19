from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class InventoryBase(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int = Field(ge=0)


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    quantity: int = Field(ge=0)
    reason: Optional[str] = None


class InventoryLogBase(BaseModel):
    product_id: int
    warehouse_id: int
    quantity_change: int
    previous_quantity: int
    new_quantity: int
    reason: Optional[str] = None


class InventoryLogCreate(InventoryLogBase):
    pass


class InventoryLogResponse(InventoryLogBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class InventoryResponse(InventoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class LowStockProduct(BaseModel):
    product_id: int
    product_name: str
    current_quantity: int
    warehouse_id: int
    warehouse_name: str

    class Config:
        from_attributes = True
