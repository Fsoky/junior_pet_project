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
    POSTGRES_DB: SecretStr
    POSTGRES_USER: SecretStr
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_HOST: SecretStr
    POSTGRES_PORT: SecretStr
    
    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_PASSWORD: SecretStr | None = None
    
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    
    AUTH_JWT: AuthJWT = AuthJWT()

    @property
    def db_url(self) -> str:
        return (
            "asyncpg://"
            f"{self.POSTGRES_USER.get_secret_value()}:{self.POSTGRES_PASSWORD.get_secret_value()}"
            f"@{self.POSTGRES_HOST.get_secret_value()}:{self.POSTGRES_PORT.get_secret_value()}"
            f"/{self.POSTGRES_DB.get_secret_value()}"
        )
    
    @property
    def redis_pwd(self) -> str | None:
        return self.REDIS_PASSWORD.get_secret_value() if self.REDIS_PASSWORD else None

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8"
    )


config = Config() # type: ignore[call-arg]
redis = redis_asyncio.Redis(
    host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.redis_pwd
)

TORTOISE_ORM = {
    "connections": {"default": config.db_url},
    "apps": {
        "models": {
            "models": ["src.db.models", "aerich.models"],
            "default_connection": "default",
            "migrations": "myapp.migrations",
        },
    },
}