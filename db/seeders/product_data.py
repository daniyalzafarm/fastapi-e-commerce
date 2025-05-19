from typing import Dict, List

CATEGORIES: List[Dict] = [
    {
        "id": 1,
        "name": "Electronics",
        "description": "Electronic devices and accessories",
    },
    {"id": 2, "name": "Clothing", "description": "Fashion and apparel items"},
    {"id": 3, "name": "Books", "description": "Books and publications"},
    {
        "id": 4,
        "name": "Home & Kitchen",
        "description": "Home appliances and kitchen essentials",
    },
]

PRODUCTS: List[Dict] = [
    {
        "id": 1,
        "category_id": 1,
        "name": "Smartphone X",
        "description": "Latest model smartphone with advanced features",
        "price": 999.99,
    },
    {
        "id": 2,
        "category_id": 1,
        "name": "Wireless Earbuds",
        "description": "High-quality wireless earbuds with noise cancellation",
        "price": 149.99,
    },
    {
        "id": 3,
        "category_id": 2,
        "name": "Men's T-Shirt",
        "description": "Comfortable cotton t-shirt for everyday wear",
        "price": 29.99,
    },
    {
        "id": 4,
        "category_id": 2,
        "name": "Women's Jeans",
        "description": "Classic fit denim jeans",
        "price": 59.99,
    },
    {
        "id": 5,
        "category_id": 3,
        "name": "Python Programming Guide",
        "description": "Comprehensive guide to Python programming",
        "price": 39.99,
    },
    {
        "id": 6,
        "category_id": 4,
        "name": "Smart Coffee Maker",
        "description": "Programmable coffee maker with smart features",
        "price": 79.99,
    },
]
