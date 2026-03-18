from typing import Any
from datetime import datetime, timedelta, timezone
import uuid

import jwt

from src.core.config import config, redis


async def encode_jwt(
    payload: dict[str, Any],
    private_key: str = config.AUTH_JWT.PRIVATE_KEY_PATH.read_text(),
    algorithm: str = config.AUTH_JWT.ALGORITHM,
    expire_minutes: int = config.AUTH_JWT.ACCESS_TOKEN_EXPIRE_MINUTES
) -> str:
    now = datetime.now(timezone.utc)
    expire = now + timedelta(minutes=expire_minutes)
    token_id = uuid.uuid4().hex
    ttl = int((expire - now).total_seconds())
    
    payload.update(exp=expire, iat=now, jti=token_id)
    await redis.set(f"token:{token_id}:{payload.get('sub')}", "alive", ttl)
    
    encoded = jwt.encode(payload, private_key, algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = config.AUTH_JWT.PUBLIC_KEY_PATH.read_text(),
    algorithm: str = config.AUTH_JWT.ALGORITHM
) -> dict[str, Any] | None:
    try:
        decoded = jwt.decode(token, public_key, [algorithm])
        return decoded
    except jwt.ExpiredSignatureError:
        return None