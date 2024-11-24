# from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from src.database.core import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name: Mapped[str] = mapped_column(String(36), nullable=False)
    last_name: Mapped[str] = mapped_column(String(36), nullable=False)
    roles = relationship("Role", secondary="user_role", back_populates="users") 