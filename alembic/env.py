import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.ext.asyncio import AsyncEngine, async_engine_from_config
from sqlalchemy.engine import Connection

from alembic import context

from app.db.base import Base  # SQLAlchemy Base model import
from app.core.config import settings  # Import settings to access database configuration

from app.models.user import User
from app.api.v1.features.sample_feature.models import SampleModel

# Alembic configuration object
config = context.config

# Configure logging based on the Alembic configuration file
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set the SQLAlchemy URL to your database URL from settings
config.set_main_option("sqlalchemy.url", str(settings.DATABASE_URL))

# Specify metadata from your SQLAlchemy models
# Alembic will use this metadata to generate migrations automatically
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in offline mode (without a database connection)."""
    context.configure(
        url=str(settings.DATABASE_URL),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run migrations using a synchronous connection (called by async wrapper)."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations in an asynchronous context."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode using an async connection."""
    asyncio.run(run_async_migrations())


# Choose whether to run migrations offline or online based on context
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

