from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_db_session

from . import auth_schemas, auth_service

router = APIRouter(prefix="/roles", tags=["roles"])


@router.get("/", response_model=List[auth_schemas.Role])
async def get_roles(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_db_session)
):
    return await auth_service.get_roles(session=session, skip=skip, limit=limit)
