from typing import List  # Importing List type for type hinting
from pydantic_settings import BaseSettings  # Importing BaseSettings from pydantic_settings for configuration management
from pydantic import AnyHttpUrl, PostgresDsn  # Importing AnyHttpUrl for validating HTTP URLs

class Settings(BaseSettings):
    """
    Configuration settings for the FastAPI project.
    Uses Pydantic's BaseSettings to load settings from environment variables.
    """

    PROJECT_NAME: str = "FastAPI Project"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:5173"]
    FIRST_SUPERUSER: str = "admin@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin123"

    # Database Settings
    DATABASE_URL: PostgresDsn

    # Auth settings
    SECRET_KEY: str = "your-secret-key" 
    
    class Config:
        """
        Pydantic configuration class.
        """
        case_sensitive = True  # Ensures environment variable names are case-sensitive
        env_file = ".env"  # Specifies the environment file to load variables from

# Instantiate the settings object, automatically loading values from the environment
settings = Settings()

