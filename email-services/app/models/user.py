from sqlalchemy import Column, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from .base import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'identity'}  # Ensure this matches the schema name
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(100), unique=True, nullable=False)
    # Other fields...
    
    # Define the relationship to the Folder model
    folders = relationship("Folder", back_populates="user")
