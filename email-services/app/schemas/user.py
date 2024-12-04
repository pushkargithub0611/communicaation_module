from pydantic import BaseModel
from typing import Optional
import datetime
from uuid import UUID

class UserBase(BaseModel):
    username: str
    email: str
    fullname: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    fullname: Optional[str] = None
    password: Optional[str] = None

class UserOut(UserBase):
    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True  # Important for SQLAlchemy to Pydantic serialization

# Add UserResponse
class UserResponse(UserOut):
    message: str  # For API responses that include a user object and a custom message
