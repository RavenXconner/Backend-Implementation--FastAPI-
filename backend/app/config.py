from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str
    CORS_ORIGINS: List[str]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
