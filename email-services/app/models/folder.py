from sqlalchemy import Column, String, TIMESTAMP, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from .base import Base

class Folder(Base):
    __tablename__ = 'folders'
    __table_args__ = {'schema': 'email'}  # Ensure this matches the schema name
    
    # Define the columns
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('identity.users.id', ondelete='CASCADE'))  # foreign key
    name = Column(String(100), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    
    # Define the relationship to the User model
    user = relationship("User", back_populates="folders")
