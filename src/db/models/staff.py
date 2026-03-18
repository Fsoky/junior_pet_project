from tortoise import fields
from tortoise.models import Model

from src.db.utils.enums import Role


class StaffMember(Model):
    id = fields.UUIDField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    role = fields.CharEnumField(Role, default=Role.EMPLOYEE)
    
    user: fields.OneToOneRelation = fields.OneToOneField("models.User", "staff_member")
    
    class Meta:
        table = "staff_members"