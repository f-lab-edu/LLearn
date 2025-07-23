from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_name: str = ""
    database_password: str = ""
    database_url: str = ""
    sqlalchemy_database_url: str = ""


@lru_cache
def get_settings():
    return Settings()
