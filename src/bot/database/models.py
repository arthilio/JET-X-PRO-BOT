from sqlalchemy import Column, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserSubscription(Base):
    __tablename__ = "subscriptions"
    
    user_id = Column(String, primary_key=True)
    gem_tier = Column(String)
    start_date = Column(DateTime)
    expiry_date = Column(DateTime)
    payment_method = Column(String)
    admin_approved = Column(Boolean, default=False)
    special_notes = Column(String)
