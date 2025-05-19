from enum import Enum


class RoleType(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"
