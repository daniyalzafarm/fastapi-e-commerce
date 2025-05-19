from typing import Dict, List

# Initial inventory data for each product in each warehouse
INVENTORY: List[Dict] = [
    # Smartphone X
    {
        "product_id": 1,
        "warehouse_id": 1,
        "quantity": 100,
    },
    {
        "product_id": 1,
        "warehouse_id": 2,
        "quantity": 75,
    },
    # Wireless Earbuds
    {
        "product_id": 2,
        "warehouse_id": 1,
        "quantity": 200,
    },
    {
        "product_id": 2,
        "warehouse_id": 3,
        "quantity": 150,
    },
    # Men's T-Shirt
    {
        "product_id": 3,
        "warehouse_id": 2,
        "quantity": 300,
    },
    {
        "product_id": 3,
        "warehouse_id": 3,
        "quantity": 250,
    },
    # Women's Jeans
    {
        "product_id": 4,
        "warehouse_id": 1,
        "quantity": 200,
    },
    {
        "product_id": 4,
        "warehouse_id": 2,
        "quantity": 180,
    },
    # Python Programming Guide
    {
        "product_id": 5,
        "warehouse_id": 1,
        "quantity": 500,
    },
    {
        "product_id": 5,
        "warehouse_id": 3,
        "quantity": 400,
    },
    # Smart Coffee Maker
    {
        "product_id": 6,
        "warehouse_id": 2,
        "quantity": 50,
    },
    {
        "product_id": 6,
        "warehouse_id": 3,
        "quantity": 30,
    },
]

# Sample inventory logs to show stock changes
INVENTORY_LOGS: List[Dict] = [
    # Smartphone X stock adjustments
    {
        "id": 1,
        "product_id": 1,
        "warehouse_id": 1,
        "quantity_change": -20,
        "previous_quantity": 120,
        "new_quantity": 100,
        "reason": "Initial stock adjustment",
    },
    {
        "id": 2,
        "product_id": 1,
        "warehouse_id": 2,
        "quantity_change": -25,
        "previous_quantity": 100,
        "new_quantity": 75,
        "reason": "Initial stock adjustment",
    },
    # Wireless Earbuds stock adjustments
    {
        "id": 3,
        "product_id": 2,
        "warehouse_id": 1,
        "quantity_change": -50,
        "previous_quantity": 250,
        "new_quantity": 200,
        "reason": "Initial stock adjustment",
    },
    {
        "id": 4,
        "product_id": 2,
        "warehouse_id": 3,
        "quantity_change": -50,
        "previous_quantity": 200,
        "new_quantity": 150,
        "reason": "Initial stock adjustment",
    },
]
