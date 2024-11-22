from src.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import UUID

class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    users = relationship("User", secondary="user_role", back_populates="roles")

class UserRole(Base):
    __tablename__ = "user_role"
    
    user_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"), primary_key=True)