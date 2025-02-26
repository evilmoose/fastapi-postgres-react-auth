from typing import AsyncGenerator
from sqlalchemy import Column, Integer, String, Boolean
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi import Depends
from app.db.base import Base, AsyncSessionLocal
from sqlalchemy.ext.asyncio import AsyncSession

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

async def get_user_db(session: AsyncSession = Depends(AsyncSessionLocal)):
    yield SQLAlchemyUserDatabase(session, User)