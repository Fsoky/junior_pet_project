from pathlib import Path

from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

import redis.asyncio as redis_asyncio

ROOT_DIR = Path(__file__).resolve().parents[2]


class AuthJWT(BaseModel):
    PRIVATE_KEY_PATH: Path = ROOT_DIR / "certs" / "private.pem"
    PUBLIC_KEY_PATH: Path = ROOT_DIR / "certs" / "public.pem"
    ALGORITHM: str = "RS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15


class Config(BaseSettings):
    DB_URL: SecretStr
    
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    
    AUTH_JWT: AuthJWT = AuthJWT()

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8"
    )


config = Config() # type: ignore[call-arg]
redis = redis_asyncio.Redis()

TORTOISE_ORM = {
    "connections": {"default": config.DB_URL.get_secret_value()},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
            "migrations": "myapp.migrations",
        },
    },
}