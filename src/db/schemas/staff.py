from pydantic import ConfigDict
from tortoise.contrib.pydantic import pydantic_model_creator

from src.db.models.staff import StaffMember

StaffMemberSchema = pydantic_model_creator(
    StaffMember,
    model_config=ConfigDict(populate_by_name=True, from_attributes=True),
)