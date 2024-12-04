# app/db/base.py
from sqlalchemy.ext.declarative import declarative_base  # Import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.db.session import SessionLocal

# Define the Base class for the declarative models
Base = declarative_base()

# Define the function to get a database session
def get_db() -> Session:
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used in FastAPI routes
    finally:
        db.close()  # Close the session when done
