from fastapi import FastAPI # Importing FastAPI
from fastapi.middleware.cors import CORSMiddleware # Importing CORSMiddleware
from app.core.config import settings # Importing settings from core.config
from app.db.base import engine, Base # Importing the database engine and base model
from app.api.v1.endpoints import users

import logging

# Set up SQLAlchemy logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME, # setting the project name
    openapi_url=f"{settings.API_V1_STR}/openapi.json" # setting the openapi_url
)

# Configure Cross-Origin Resource Sharing (CORS) settings
# This allows external frontend applications to access the API securely
app.add_middleware(
    CORSMiddleware,
    # Convert list of allowed origins to strings
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True, # Allow credentials (cookies, authorization headers)
    allow_methods=["*"], # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Allow all headers in requests
)

# Include routers
app.include_router(users.router, prefix=settings.API_V1_STR)


# Root endpoint - returns a welcome message
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI"}

# Health check endpoint - useful for monitoring if the API is running
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.on_event("startup")
async def startup():
    # Create database tables
    print("[Startup] Initializing database...")
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)  # Uncomment to reset tables
        await conn.run_sync(Base.metadata.create_all)
        print("[Startup] Database tables created/verified")

@app.on_event("shutdown")
async def shutdown():
    # Close database connection
    await engine.dispose()