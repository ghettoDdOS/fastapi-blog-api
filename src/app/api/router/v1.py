from fastapi import APIRouter

from app.blog import blog_v1_router

router = APIRouter()

router.include_router(blog_v1_router, prefix="/blog", tags=("blog",))
