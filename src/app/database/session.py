from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from app.core.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
)
session = AsyncSession(engine, expire_on_commit=False)
