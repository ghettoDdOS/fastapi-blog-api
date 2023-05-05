from fastapi import APIRouter

from .views import author

blog_v1_router = APIRouter()

blog_v1_router.include_router(
    author.router,
    prefix="/authors",
)
