from pydantic_settings import BaseSettings

class Settings(BaseSettings): 
    ENVIRONMENT: str = "development"