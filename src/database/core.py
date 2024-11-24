from typing import Annotated, AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from src.settings import Settings
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

settings = Settings()

# Check if development environment
is_production = settings.ENVIRONMENT == "production" 

DB_URL = 'postgresql+asyncpg://postgres:123@localhost:5433/cintasii-fastapi'

engine = create_async_engine(DB_URL)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False) 

# Create a new base
Base = declarative_base()

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_db() -> AsyncGenerator[AsyncSession, None]: 
    async with async_session_maker() as session:
        yield session

DbSession = Annotated[AsyncSession, Depends(get_db)]