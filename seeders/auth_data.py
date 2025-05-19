from typing import Dict, List

from src.auth import RoleType

ROLES: List[Dict] = [
    {"id": 1, "name": RoleType.ADMIN},
    {"id": 2, "name": RoleType.CUSTOMER},
]

USERS: List[Dict] = [
    {
        "id": 1,
        "name": "Admin User",
        "email": "admin@example.com",
        "phone": None,
        "address": None,
        "role_id": 1,
    },
    {
        "id": 2,
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "+1234567890",
        "address": "123 Main St",
        "role_id": 2,
    },
    {
        "id": 3,
        "name": "Jane Smith",
        "email": "jane@example.com",
        "phone": "+0987654321",
        "address": "456 Oak Ave",
        "role_id": 2,
    },
]
