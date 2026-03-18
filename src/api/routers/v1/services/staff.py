from src.api.core.base_service import BaseService, ServiceResponse

from src.api.routers.v1.schemas import AddNewEmployeeSchema, UpdateEmployeeSchema

from src.db.models import User, StaffMember
from src.db.schemas import StaffMemberSchema, UserSchema
from src.db.utils.enums import Role


class StaffService(BaseService):
    """Staff service
    
    Пользователь ставший сотрудником (employee), может быть повышен до админинстратора (admin),
    только тем пользователем, у которого есть права супер-администратора (superadmin).
    
    - employee НЕ может вторгаться в процесс изменения/удаления данных сотрудников. (403)
    - admin НЕ может повышать employee до admin
    - admin НЕ может изменить роль или удалить другого admin или superadmin
    """
    
    async def get_staff(self) -> ServiceResponse:
        staff_members = await StaffMember.all().select_related("user")
        staff_member_objs = [
            {
                **(
                    await StaffMemberSchema.from_tortoise_orm(member)
                ).model_dump(mode="json", exclude={"created_at", "updated_at"}),
                "user": (
                    await UserSchema.from_tortoise_orm(member.user)
                ).model_dump(mode="json", exclude={"created_at", "updated_at"})
            }
            for member in staff_members
        ]
        
        return self.ok(staff_member_objs)
    
    async def add_new_employee(
        self, admin: StaffMember, schema: AddNewEmployeeSchema
    ) -> ServiceResponse:
        user = (
            await User
            .filter(id=schema.user_id, is_active=True)
            .first()
            .prefetch_related("staff_member")
        )
        
        if not user:
            return self.error("User not found or inactive")
        if user.staff_member:
            return self.error("Member already exists")
        if admin.role == Role.ADMIN and schema.role >= Role.ADMIN:
            return self.error("You cannot add new members with admin, superadmin roles")
        
        await StaffMember.create(**schema.model_dump())
        return self.ok(message="New member successfully added")
    
    async def update_employee(
        self, id: str, admin: StaffMember, schema: UpdateEmployeeSchema
    ) -> ServiceResponse:
        employee = await StaffMember.filter(id=id, user__is_active=True).first()
        
        if not employee:
            return self.error("Member not found or user inactive")
        if admin.role <= employee.role:
            return self.error("You cannot update members with admin, superadmin roles")
        
        employee.update_from_dict(schema.model_dump(exclude_unset=True, exclude_none=True))
        await employee.save()
        
        return self.ok(message="Member successfully updated")
    
    async def delete_employee(self, id: str, admin: StaffMember) -> ServiceResponse:
        employee = await StaffMember.filter(id=id, user__is_active=True).first()
        
        if not employee:
            return self.error("Member not found or user inactive")
        if admin.role <= employee.role:
            return self.error("You cannot delete members with admin, superadmin roles")
        
        await employee.delete()
        return self.ok("Member successfully deleted")