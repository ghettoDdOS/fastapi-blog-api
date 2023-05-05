#!/usr/bin/env python
"""Command-line utility for administrative tasks."""
from typing import Optional

import typer
import uvicorn
from alembic import command
from alembic.config import Config

from app.core.config import settings

app = typer.Typer()

alembic_config = Config(settings.paths.PROJECT_DIR / "alembic.ini")


@app.command()
def runserver():
    uvicorn.run(
        "app.core.app:app",
        host="localhost",
        port=8080,
        reload=True,
    )


@app.command()
def makemigrations(message: Optional[str] = None):
    command.revision(alembic_config, message, autogenerate=True)


@app.command()
def migrate(revision: str = "head"):
    command.upgrade(alembic_config, revision)


if __name__ == "__main__":
    app()
