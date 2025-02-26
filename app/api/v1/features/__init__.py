from fastapi import APIRouter

# Import feature routers
from .sample_feature.endpoints import router as sample_router

# Create features router
features_router = APIRouter()

# Register feature routers
features_router.include_router(
    sample_router,
    prefix="/sample",
    tags=["sample"]
)

# Function to get all feature routers
def get_features_router():
    return features_router
