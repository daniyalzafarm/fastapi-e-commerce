from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.auth import auth_models
from .auth_data import ROLES, USERS

async def seed_roles(session: AsyncSession):
    """Seed the roles table with default roles"""
    query = select(auth_models.Role.id)
    result = await session.execute(query)
    existing_role_ids = {role[0] for role in result.fetchall()}
    
    for role_data in ROLES:
        if role_data["id"] not in existing_role_ids:
            role = auth_models.Role(**role_data)
            session.add(role)

    await session.commit()

async def seed_users(session: AsyncSession):
    """Seed the users table with default users"""
    query = select(auth_models.User.id)
    result = await session.execute(query)
    existing_user_ids = {user[0] for user in result.fetchall()}
    
    for user_data in USERS:
        if user_data["id"] not in existing_user_ids:
            user = auth_models.User(**user_data)
            session.add(user)
    
    await session.commit()

async def seed_auth_data(session: AsyncSession):
    """Seed all auth-related data"""
    await seed_roles(session)
    await seed_users(session)
