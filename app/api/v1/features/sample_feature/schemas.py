# app/api/v1/features/sample-feature/schemas.py
from pydantic import BaseModel
from typing import Optional

# Shared properties
class SampleItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

# Properties to receive on item creation
class SampleItemCreate(SampleItemBase):
    title: str

# Properties to receive on item update
class SampleItemUpdate(SampleItemBase):
    pass

# Properties shared by models stored in DB
class SampleItemInDBBase(SampleItemBase):
    id: int
    user_id: int
    
    class Config:
        orm_mode = True

# Properties to return to client
class SampleItem(SampleItemInDBBase):
    pass