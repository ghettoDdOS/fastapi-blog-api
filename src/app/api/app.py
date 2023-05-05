from fastapi import FastAPI

from .router import v1

app = FastAPI(root_path="/api", docs_url="/")

app.include_router(v1.router)
