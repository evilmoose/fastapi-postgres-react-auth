# app/models/relationships.py
from app.models.user import User
from app.api.v1.features.sample_feature.models import SampleModel
from sqlalchemy.orm import relationship

# Add the relationship to User model
User.sample_items = relationship("SampleModel", back_populates="user")