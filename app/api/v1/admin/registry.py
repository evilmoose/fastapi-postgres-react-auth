from fastapi import APIRouter

class AdminFeatureRegistry:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AdminFeatureRegistry, cls).__new__(cls)
            cls._instance.features = {}
            cls._instance.router = APIRouter()
        return cls._instance
    
    def register_feature(self, feature_name: str, feature_router: APIRouter, metadata: dict = None):
        """Register a feature's admin router"""
        self.features[feature_name] = {
            "router": feature_router,
            "metadata": metadata or {}
        }
        self.router.include_router(
            feature_router,
            prefix=f"/{feature_name}",
            tags=[f"admin-{feature_name}"]
        )
    
    def get_features(self):
        """Get all registered admin features"""
        return self.features
    
    def get_router(self):
        """Get the combined router with all feature admin endpoints"""
        return self.router

# Singleton instance
admin_registry = AdminFeatureRegistry()
