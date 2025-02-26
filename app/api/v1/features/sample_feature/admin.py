from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session_local
from app.api.v1.admin import admin_required
from . import models, schemas

admin_router = APIRouter()

@admin_router.get("/stats")
async def sample_feature_stats(
    db: AsyncSession = Depends(get_session_local),
    current_user = Depends(admin_required)
):
    """Get statistics for sample feature"""
    # Count total items
    result = await db.execute("SELECT COUNT(*) FROM sample_items")
    total_items = result.scalar()
    
    # Get items per user
    result = await db.execute("""
        SELECT user_id, COUNT(*) as item_count 
        FROM sample_items 
        GROUP BY user_id 
        ORDER BY item_count DESC
        LIMIT 5
    """)
    top_users = [{"user_id": row[0], "item_count": row[1]} for row in result]
    
    return {
        "total_items": total_items,
        "top_users": top_users
    }

@admin_router.get("/items")
async def list_all_items(
    db: AsyncSession = Depends(get_session_local),
    current_user = Depends(admin_required),
    skip: int = 0,
    limit: int = 100
):
    """List all items (admin only)"""
    result = await db.execute(
        db.query(models.SampleModel)
        .offset(skip)
        .limit(limit)
    )
    items = result.scalars().all()
    return items
