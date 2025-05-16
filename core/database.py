from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from core.config import env

engine = create_async_engine(env.db_url, echo=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))
    print("=== Database connection successful. ===")
