from pydantic import ConfigDict
from tortoise.contrib.pydantic import pydantic_model_creator

from src.db.models.user import User

UserSchema = pydantic_model_creator(
    User,
    model_config=ConfigDict(populate_by_name=True, from_attributes=True),
    exclude=("password",) # Исключаем пароль по умолчанию
)