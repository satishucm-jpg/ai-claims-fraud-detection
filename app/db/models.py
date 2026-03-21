from sqlalchemy import Column, Integer, Float
from app.db.database import Base

class ClaimRecord(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    age = Column(Integer)
    claim_type = Column(Integer)
    fraud = Column(Integer)