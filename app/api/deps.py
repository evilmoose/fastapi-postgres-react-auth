# app/api/deps.py
from typing import List, AsyncGenerator
from fastapi import HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.auth.users import current_active_user as get_current_user
from app.db.session import get_session_local
import warnings

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    @deprecated Use get_session_local from app.db.session instead.
    This will be removed in a future version.
    """
    warnings.warn(
        "get_db is deprecated. Use get_session_local from app.db.session instead.",
        DeprecationWarning,
        stacklevel=2
    )
    async for session in get_session_local():
        yield session

def get_current_user_with_roles(required_roles: List[str] = None):
    """
    Dependency to get current user with role check.
    """
    async def current_user_with_roles(
        current_user: User = Depends(get_current_user)
    ) -> User:
        if required_roles:
            for role in required_roles:
                if role not in current_user.roles:
                    raise HTTPException(
                        status_code=403,
                        detail=f"User doesn't have required role: {role}"
                    )
        return current_user
    
    return current_user_with_roles