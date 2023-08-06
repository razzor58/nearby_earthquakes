import pathlib

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_URL: AnyHttpUrl

    class Config:
        env_file = pathlib.Path(pathlib.Path(__file__).parent.parent, ".env")


settings = Settings()
