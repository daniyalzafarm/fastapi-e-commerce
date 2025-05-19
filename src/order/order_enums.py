from enum import Enum


class OrderStatus(str, Enum):
    """Enum for order statuses"""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"
