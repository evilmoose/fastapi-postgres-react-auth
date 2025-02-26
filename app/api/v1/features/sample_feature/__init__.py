# app/api/v1/features/sample_feature/__init__.py
from fastapi import APIRouter
from .endpoints import router
from .admin import admin_router
from app.api.v1.admin.registry import admin_registry

# Register the feature's admin router
admin_registry.register_feature(
    "sample_feature", 
    admin_router,
    metadata={
        "display_name": "Sample Feature",
        "description": "Manage sample items and view statistics",
        "icon": "chart-bar"
    }
)

# Export the main feature router
def get_router():
    return router
