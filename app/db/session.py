from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.base import AsyncSessionLocal  # Import session factory from base.py

# Dependency to provide DB session
async def get_session_local() -> AsyncGenerator[AsyncSession, None]:
    print("[Database] Opening new database session")
    async with AsyncSessionLocal() as session:
        try:
            yield session  # Provide session to API endpoints
            await session.commit()  # Commit after successful operation
            print("[Database] Session committed successfully")
        except Exception:
            await session.rollback()  # Roll back on error
            # print(f"[Database] Error in session, rolling back: {str(e)}")
            raise
        finally:
            await session.close()  # Close session when done
            print("[Database] Session closed")
