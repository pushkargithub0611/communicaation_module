# app/core/config.py

import os

class Settings:
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/email_service')
    JWT_SECRET_KEY: str = os.getenv('JWT_SECRET_KEY', 'your_secret_key')
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
