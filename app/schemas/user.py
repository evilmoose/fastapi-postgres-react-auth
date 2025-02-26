# app/schemas/user.py
from typing import Optional, List
from pydantic import BaseModel, EmailStr
from fastapi_users import schemas

class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    roles: List[str] = ["user"]

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
            }
        }

class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "strongpassword123",
            }
        }