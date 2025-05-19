from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import auth_models, auth_schemas


async def get_roles(
    session: AsyncSession, skip: int = 0, limit: int = 100
) -> List[auth_models.Role]:
    query = select(auth_models.Role).offset(skip).limit(limit)
    result = await session.execute(query)
    return result.scalars().all()


async def create_user(
    session: AsyncSession, user: auth_schemas.UserCreate
) -> auth_models.User:
    db_user = auth_models.User(**user.model_dump())
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def get_users(
    session: AsyncSession, skip: int = 0, limit: int = 100
) -> List[auth_models.User]:
    query = select(auth_models.User).offset(skip).limit(limit)
    result = await session.execute(query)
    return result.scalars().all()


async def get_user_by_id(session: AsyncSession, user_id: int) -> auth_models.User:
    query = select(auth_models.User).filter(auth_models.User.id == user_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()
