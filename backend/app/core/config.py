from pydantic_settings import BaseSettings
import os

# If you don't have a .env file, you can set the variables in your environment
# For local development, create a .env file in the `backend` directory

class Settings(BaseSettings):
    # Core application settings
    APP_NAME: str = "Autonomous Call Center"
    DEBUG: bool = False

    # Gemini API Key
    GEMINI_API_KEY: str = "YOUR_GEMINI_API_KEY_HERE"

    # MongoDB settings
    MONGO_URI: str = "mongodb://mongo:27017/"
    MONGO_DB_NAME: str = "call_center_db"

    # Qdrant settings
    QDRANT_URL: str = "http://qdrant:6333"
    QDRANT_API_KEY: str | None = None # Set if you have an API key

    # JWT Authentication settings
    JWT_SECRET_KEY: str = "a_very_secret_key"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # This tells Pydantic to load variables from a .env file
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Create a single instance of the settings to be used throughout the application
settings = Settings()
