from fastapi import FastAPI
from dotenv import load_dotenv
from src.logging.log_config import logger
from fastapi.middleware.cors import CORSMiddleware 
from src.api.api import router as api_router
from src.database.manage import init_database
from src.database.core import engine
from src.settings import Settings  
from src.database.manage import init_database

load_dotenv()


settings = Settings()

is_production = settings.ENVIRONMENT == "production"

app = FastAPI(title="Cintasii API",debug=not is_production,version="v1.0.0")

logger.info('API is starting up') 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)
 
app.include_router(router=api_router, prefix="/api")