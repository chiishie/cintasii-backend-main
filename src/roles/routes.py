from uuid import UUID
from fastapi import APIRouter, Depends
from src.database.core import DbSession, get_db
from src.roles.schemas import RoleCreate
import src.roles.service as role_service


router = APIRouter()

@router.post("/")
async def create_role(role: RoleCreate, db: DbSession):
    return await role_service.create_role(role, db)

@router.get("/")
async def get_roles(db: DbSession):
    return await role_service.get_roles(db)

@router.post("/assign")
async def assign_role_to_user(user_id: UUID, role_id: int, db: DbSession):
    return await role_service.assign_role_to_user(user_id, role_id, db)

@router.get("/user/{user_id}")
async def get_user_roles(user_id: UUID, db: DbSession):
    return await role_service.get_user_roles(user_id, db)

