from pathlib import Path

from pydantic import BaseSettings, PostgresDsn


class PathSettings(BaseSettings):
    CONFIG_DIR = Path(__file__).parent
    SRC_DIR = CONFIG_DIR.parent
    PROJECT_DIR = SRC_DIR.parent


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn

    paths = PathSettings()

    class Config:
        env_file = ".env"


settings = Settings()
