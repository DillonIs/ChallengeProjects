# Config file for secure TaskManager
from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv("/root/ChallengeProjects/SecureTaskManagement/Backend/.env")

class Settings(BaseSettings):
    # PostgreSQL
    DATABASE_URL: str

    # App secret key
    SECRET_KEY: str

    # Cookie/session settings
    SESSION_COOKIE_NAME: str = "session_id"
    SESSION_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 Days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Debug
    DEBUG: bool = True

    class Config:
        env_file = "/root/ChallengeProjects/SecureTaskManagement/Backend/.env"
        env_file_encoding = "utf-8"
        extra = "ignore"

# Create setting instance
settings = Settings()