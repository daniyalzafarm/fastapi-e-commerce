from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from . import auth_schemas, auth_service
from src.db import get_db_session

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=auth_schemas.User)
async def create_user(user: auth_schemas.UserCreate, session: AsyncSession = Depends(get_db_session)):
    return await auth_service.create_user(session=session, user=user)

@router.get("/", response_model=List[auth_schemas.User])
async def get_users(skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_db_session)):
    return await auth_service.get_users(session=session, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=auth_schemas.User)
async def get_user(user_id: int, session: AsyncSession = Depends(get_db_session)):
    user = await auth_service.get_user_by_id(session=session, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
