from sqlalchemy.ext.asyncio import AsyncSession

from app.database import async_session


async def get_session() -> AsyncSession:
    session = async_session()
    try:
        yield session
    finally:
        await session.close()
