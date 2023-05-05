import sqlalchemy as sa
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Author
from ..schemes import AuthorRequest


class AuthorCRUD:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, author: AuthorRequest) -> Author:
        instance = Author(**author.dict())
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def get_all(self) -> list[Author]:
        query = sa.select(Author)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by_id(self, id: int, raise_execptions=True) -> Author | None:
        query = sa.select(Author).where(Author.id == id)
        result = await self.session.execute(query)
        instance = result.scalar_one_or_none()
        if raise_execptions and instance is None:
            raise HTTPException(
                status_code=404, detail=f"Пользователь с id {id} не найден"
            )
        return instance

    async def delete(self, id: int) -> None:
        instance = await self.get_by_id(id)
        query = sa.delete(Author).where(Author.id == instance.id)
        await self.session.execute(query)
