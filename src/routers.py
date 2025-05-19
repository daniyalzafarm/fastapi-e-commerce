from fastapi import FastAPI

from src.auth import role_router, user_router
from src.inventory import inventory_router
from src.order import order_router
from src.product import product_router


def include_routers(app: FastAPI) -> None:
    app.include_router(role_router)
    app.include_router(user_router)
    app.include_router(product_router)
    app.include_router(order_router)
    app.include_router(inventory_router)
