from fastapi import APIRouter
from .endpoints import users
from .features import get_features_router
from .admin import get_admin_router
from .admin.registry import admin_registry

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(get_features_router(), prefix="/features")

# Include admin routers
api_router.include_router(get_admin_router(), prefix="/admin")
api_router.include_router(admin_registry.get_router(), prefix="/admin/features")

# Export the router
def get_api_router():
    return api_router
