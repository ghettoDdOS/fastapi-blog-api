from fastapi import FastAPI

from app.api import api_app

app = FastAPI(docs_url=None)

app.mount("/api", api_app)
