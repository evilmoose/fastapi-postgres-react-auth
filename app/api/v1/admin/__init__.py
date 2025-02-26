from fastapi import APIRouter, Depends
from app.api.deps import get_current_user_with_roles

admin_router = APIRouter()

# Admin-only middleware
async def admin_required(current_user = Depends(get_current_user_with_roles(["admin"]))):
    return current_user

# Core admin endpoints
@admin_router.get("/dashboard")
async def admin_dashboard(current_user = Depends(admin_required)):
    """
    Get admin dashboard data
    """
    return {
        "total_users": 100,  # Replace with actual query
        "active_features": ["sample_feature"],  # Dynamic list of active features
        "system_status": "healthy"
    }

# Function to get admin router
def get_admin_router():
    return admin_router
