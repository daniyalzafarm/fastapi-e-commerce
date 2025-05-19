from fastapi import FastAPI
from src.auth import role_router
from src.auth import user_router

def include_routers(app: FastAPI) -> None:
    app.include_router(role_router)
    app.include_router(user_router)
