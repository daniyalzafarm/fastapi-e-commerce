from fastapi import FastAPI
from core.config import env
from contextlib import asynccontextmanager
from sqlalchemy.exc import SQLAlchemyError
from src.db import init_db, engine

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

@app.get("/")
def read_root():
    return {"message": "Welcome to E-commerce API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=env.host, port=env.port)