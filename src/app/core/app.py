from fastapi import FastAPI

from app.api import api_router

app = FastAPI(docs_url="/api")


app.include_router(api_router, prefix="/api")
