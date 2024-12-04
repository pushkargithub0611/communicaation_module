# app/models/identity.py

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.db.base import Base
import uuid
import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    fullname = Column(String)
    created_at = Column(String, default=datetime.datetime.utcnow)
    updated_at = Column(String, default=datetime.datetime.utcnow)
    
    roles = relationship("Role", secondary="user_roles")

class Role(Base):
    __tablename__ = 'roles'
    
    id = Column(UUID, primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, unique=True)

class UserRole(Base):
    __tablename__ = 'user_roles'
    
    user_id = Column(UUID, ForeignKey('users.id'), primary_key=True)
    role_id = Column(UUID, ForeignKey('roles.id'), primary_key=True)
