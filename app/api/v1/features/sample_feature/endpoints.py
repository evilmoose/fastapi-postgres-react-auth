from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api import deps
from app.models.user import User
from . import models, schemas

router = APIRouter()

@router.get("/", response_model=List[schemas.SampleItem])
def read_sample_items(
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    skip: int = 0,
    limit: int = 100,
):
    """
    Retrieve sample items for the current user.
    """
    items = db.query(models.SampleModel).filter(
        models.SampleModel.user_id == current_user.id
    ).offset(skip).limit(limit).all()
    return items

@router.post("/", response_model=schemas.SampleItem)
def create_sample_item(
    *,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
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
    db.commit()
    db.refresh(item)
    return item

@router.get("/{item_id}", response_model=schemas.SampleItem)
def read_sample_item(
    *,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
    item_id: int,
):
    """
    Get sample item by ID.
    """
    item = db.query(models.SampleModel).filter(
        models.SampleModel.id == item_id,
        models.SampleModel.user_id == current_user.id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
