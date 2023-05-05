from fastapi import APIRouter

from app.blog.v1 import blog_v1_router

api_v1_router = APIRouter()
api_v1_router.include_router(blog_v1_router, prefix="/blog", tags=("blog",))
