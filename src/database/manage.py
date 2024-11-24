from .core import Base, engine
from src.logging.log_config import logger

async def init_database():
    logger.info('Creating tables')
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)