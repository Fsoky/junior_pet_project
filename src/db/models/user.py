from tortoise import fields
from tortoise.models import Model

from .staff import StaffMember


class User(Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    surname = fields.CharField(64)
    middle_name = fields.CharField(64)
    email = fields.CharField(256)
    password = fields.CharField(128)
    is_active = fields.BooleanField(default=True)
    
    staff_member: fields.ReverseRelation[StaffMember]
    
    class Meta:
        table = "users"