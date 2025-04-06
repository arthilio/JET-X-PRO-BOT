from sqlalchemy import Column, Integer, String
from app.database import Base

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String)
    away_team = Column(String)
    predicted_score = Column(String)
    confidence = Column(String)
