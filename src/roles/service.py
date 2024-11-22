from uuid import UUID
from sqlalchemy import insert, select
from src.roles.schemas import RoleCreate
from src.roles.models import Role, UserRole
from src.database.core import DbSession


async def create_role(role: RoleCreate, db: DbSession):
    role = Role(name=role.name)
    db.add(role)
    await db.commit()
    return role

async def get_roles(db: DbSession):
    stmt = select(Role)
    result = await db.execute(stmt)
    return result.scalars().all()

async def assign_role_to_user(user_id: UUID, role_id: int, db: DbSession):
    stmt = insert(UserRole).values(user_id=user_id, role_id=role_id)
    await db.execute(stmt)
    await db.commit()

async def get_user_roles(user_id: UUID, db: DbSession):
    stmt = select(Role).join(UserRole).filter(UserRole.user_id == user_id)
    result = await db.execute(stmt)
    return result.scalars().all()

