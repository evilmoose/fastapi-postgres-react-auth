# app/api/v1/features/sample-feature/endpoints.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session_local
from app.models.user import User
from . import models, schemas
from app.api.deps import get_current_user_with_roles

router = APIRouter()

@router.get("/", response_model=List[schemas.SampleItem])
async def read_sample_items(
    db: AsyncSession = Depends(get_session_local),
    current_user: User = Depends(get_current_user_with_roles(["user"])),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve sample items for the current user.
    """
    result = await db.execute(
        db.query(models.SampleModel)
        .filter(models.SampleModel.user_id == current_user.id)
        .offset(skip)
        .limit(limit)
    )
    return result.scalars().all()

@router.post("/", response_model=schemas.SampleItem)
async def create_sample_item(
    *,
    db: AsyncSession = Depends(get_session_local),
    current_user: User = Depends(get_current_user_with_roles(["user"])),
    item_in: schemas.SampleItemCreate,
):
    """
    Create new sample item.
    """
    item = models.SampleModel(
        title=item_in.title,
        description=item_in.description,
        user_id=current_user.id
    )
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item

@router.get("/{item_id}", response_model=schemas.SampleItem)
async def read_sample_item(
    *,
    db: AsyncSession = Depends(get_session_local),
    current_user: User = Depends(get_current_user_with_roles(["user"])),
    item_id: int,
):
    """
    Get sample item by ID.
    """
    result = await db.execute(
        db.query(models.SampleModel)
        .filter(
            models.SampleModel.id == item_id,
            models.SampleModel.user_id == current_user.id
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sample_item(
    *,
    db: AsyncSession = Depends(get_session_local),
    current_user: User = Depends(get_current_user_with_roles(["admin"])),
    item_id: int,
):
    """
    Delete a sample item (admin only).
    """
    result = await db.execute(
        db.query(models.SampleModel).filter(models.SampleModel.id == item_id)
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    await db.delete(item)
    await db.commit()
    return None
