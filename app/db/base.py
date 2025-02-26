from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config import settings # Import settings to get the database connection URL


# Create an async engine for connecting to the database
engine = create_async_engine(
    str(settings.DATABASE_URL), # Convert PostgresDsn to string
    echo=True, # Enables SQL query logging (set to False in production for performance)
    future=True # Ensures compatibility with SQLAlchemy 2.0 API
)

# Create an async session factory that will be used for database transactions
AsyncSessionLocal = sessionmaker(
    engine, # Bind the session to the async engine
    class_=AsyncSession, # Use the AsyncSession class for database operations
    expire_on_commit=False # Don't expire sessions on commit
)

# Base class for defining ORM models (tables)
Base = declarative_base()

# Import all models here for Alembic to discover them
from app.models.user import User  # noqa
