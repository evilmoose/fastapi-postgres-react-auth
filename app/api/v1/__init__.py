from fastapi import APIRouter
from .endpoints import users
from .features import get_features_router

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(get_features_router(), prefix="/features")

# Export the router
def get_api_router():
    return api_router
