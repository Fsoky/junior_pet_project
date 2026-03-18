from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.api.core.dependencies import check_is_staff_employee
from src.api.core.dependencies import StaffAdmin

from src.api.routers.v1.services import StaffService
from src.api.routers.v1.schemas import AddNewEmployeeSchema, UpdateEmployeeSchema

router = APIRouter(
    prefix="/staff", tags=["Staff"], dependencies=[Depends(check_is_staff_employee)]
)
service = StaffService()


@router.get("")
async def get_staff() -> JSONResponse:
    res = await service.get_staff()
    return JSONResponse(**res.response())


@router.post("/employees")
async def add_new_employee(
    admin: StaffAdmin,
    schema: AddNewEmployeeSchema = Depends(AddNewEmployeeSchema.as_form)
) -> JSONResponse:
    res = await service.add_new_employee(admin, schema)
    return JSONResponse(**res.response())


@router.put("/employees/{id}")
async def update_employee(
    id: str,
    admin: StaffAdmin,
    schema: UpdateEmployeeSchema = Depends(UpdateEmployeeSchema.as_form)
) -> JSONResponse:
    res = await service.update_employee(id, admin, schema)
    return JSONResponse(**res.response())


@router.delete("/employees/{id}")
async def delete_employee(id: str, admin: StaffAdmin) -> JSONResponse:
    res = await service.delete_employee(id, admin)
    return JSONResponse(**res.response())