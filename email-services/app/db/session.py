# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database URL (e.g., PostgreSQL, MySQL)
DATABASE_URL = "postgresql://postgres:postgres@localhost/email_service"

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a configured session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
