# app/api/v1/email_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.controllers.email_controller import create_folder, create_message, get_user_messages
from app.schemas.email import MessageCreate, FolderCreate, MessageResponse
from typing import List
import uuid

router = APIRouter()

# Create a new folder
@router.post("/folders/", response_model=FolderCreate)
def add_folder(folder: FolderCreate, db: Session = Depends(get_db), user_id: str = "default_user"):
    return create_folder(db, folder, user_id)

# Send a new message
@router.post("/messages/", response_model=MessageResponse)
def add_message(message: MessageCreate, db: Session = Depends(get_db), user_id: str = "default_user"):
    return create_message(db, message, user_id)

# Retrieve all messages for a user
@router.get("/messages/", response_model=List[MessageResponse])
def get_messages(db: Session = Depends(get_db), user_id: str = "default_user"):
    messages = get_user_messages(db, user_id)
    if not messages:
        raise HTTPException(status_code=404, detail="No messages found")
    return messages
