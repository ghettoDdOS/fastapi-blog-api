from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_session

from ...schemes import AuthorRequest, AuthorResponse
from ...services import AuthorCRUD

router = APIRouter()


@router.post("/", response_model=AuthorResponse)
async def create_author(
    author: AuthorRequest,
    session: AsyncSession = Depends(get_session),
):
    crud = AuthorCRUD(session)
    instance = await crud.create(author)
    return AuthorResponse.from_orm(instance)


@router.get("/", response_model=list[AuthorResponse])
async def get_all_authors(
    session: AsyncSession = Depends(get_session),
):
    crud = AuthorCRUD(session)
    authors = await crud.get_all()
    return [AuthorResponse.from_orm(a) for a in authors]


@router.get(
    "/{author_id}",
    response_model=AuthorResponse,
    # responses={404: {"model": Status}},
)
async def get_author(
    author_id: int,
    session: AsyncSession = Depends(get_session),
):
    crud = AuthorCRUD(session)
    instance = await crud.get_by_id(author_id)
    if instance is None:
        raise HTTPException(
            status_code=404, detail=f"Пользователь с id {author_id} не найден"
        )
    return AuthorResponse.from_orm(instance)


@router.delete(
    "/{author_id}",
    # response_model=Status,
    # responses={404: {"model": Status}},
)
async def delete_author(
    author_id: int,
    session: AsyncSession = Depends(get_session),
):
    crud = AuthorCRUD(session)
    await crud.delete(author_id)
    # return Status(detail=f"Пользователь с id {author_id} успешно удален")
