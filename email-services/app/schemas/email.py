# app/schemas/email.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FolderCreate(BaseModel):
    name: str

class MessageCreate(BaseModel):
    subject: str
    body: str
    folder_id: Optional[str] = None

class MessageResponse(BaseModel):
    id: str
    subject: str
    body: str
    sent_at: datetime
    is_read: bool

    class Config:
        orm_mode = True
