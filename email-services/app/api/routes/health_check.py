from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text  # Import the text function
from app.db.base import get_db

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Use the `text` function to execute a raw SQL query
        db.execute(text('SELECT 1'))
        return {"status": "ok", "message": "Database is connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")
