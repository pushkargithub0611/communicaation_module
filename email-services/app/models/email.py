# app/models/email.py

from sqlalchemy import Column, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
import datetime

class Folder(Base):
    __tablename__ = 'folders'
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey('identity.users.id'))
    name = Column(String, index=True)
    created_at = Column(String, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="folders")
    messages = relationship("Message", back_populates="folder")

class Message(Base):
    __tablename__ = 'messages'
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID, ForeignKey('identity.users.id'))
    subject = Column(String)
    body = Column(Text)
    sent_at = Column(String, default=datetime.datetime.utcnow)
    folder_id = Column(UUID, ForeignKey('email.folders.id'))
    is_read = Column(Boolean, default=False)

    folder = relationship("Folder", back_populates="messages")
    recipients = relationship("User", secondary="message_recipients")
    attachments = relationship("Attachment", back_populates="message")

class MessageRecipient(Base):
    __tablename__ = 'message_recipients'
    
    message_id = Column(UUID, ForeignKey('email.messages.id'), primary_key=True)
    user_id = Column(UUID, ForeignKey('identity.users.id'), primary_key=True)

class Attachment(Base):
    __tablename__ = 'attachments'
    
    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    message_id = Column(UUID, ForeignKey('email.messages.id'))
    file_name = Column(String)
    file_data = Column(Text)
