from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError

from core.config import env
from src.db import engine, init_db
from src.models import *  # This ensures all models are registered
from src.routers import include_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await init_db()
        yield
    except SQLAlchemyError as e:
        print(f"=== Failed to connect to database: {str(e)} ===")
        raise
    finally:
        await engine.dispose()
        print("=== Database connection closed ===")


app = FastAPI(lifespan=lifespan)

# Include all routers
include_routers(app)


@app.get("/")
def read_root():
    return {"message": "Welcome to E-commerce API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=env.host, port=env.port)
