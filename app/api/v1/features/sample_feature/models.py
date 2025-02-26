# app/api/v1/features/sample-feature/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class SampleModel(Base):
    __tablename__ = "sample_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationship to user
    user = relationship("User", back_populates="sample_items")