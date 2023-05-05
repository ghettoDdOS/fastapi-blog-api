from fastapi import APIRouter

from .views import author

router = APIRouter()

router.include_router(
    author.router,
    prefix="/authors",
)
