# app/controllers/email_controller.py
from sqlalchemy.orm import Session
from app.models.email import Folder, Message
from app.schemas.email import MessageCreate, FolderCreate

def create_folder(db: Session, folder_data: FolderCreate, user_id: str):
    folder = Folder(**folder_data.dict(), user_id=user_id)
    db.add(folder)
    db.commit()
    db.refresh(folder)
    return folder

def create_message(db: Session, message_data: MessageCreate, user_id: str):
    message = Message(**message_data.dict(), user_id=user_id)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_user_messages(db: Session, user_id: str):
    return db.query(Message).filter(Message.user_id == user_id).all()
