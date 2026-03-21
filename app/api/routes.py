from fastapi import APIRouter
from app.schemas.claim_schema import Claim
from app.services.prediction_service import predict_fraud
from app.db.database import SessionLocal
from app.db.models import ClaimRecord

router = APIRouter()

@router.get("/")
def home():
    return {"message": "AI Fraud Detection API Running 🚀"}

@router.post("/predict")
def predict(claim: Claim):
    result = predict_fraud(claim.amount, claim.age, claim.claim_type)
    return {"fraud": result}

@router.get("/history")
def get_history():
    db = SessionLocal()
    records = db.query(ClaimRecord).all()
    db.close()

    return [
        {
            "id": r.id,
            "amount": r.amount,
            "age": r.age,
            "claim_type": r.claim_type,
            "fraud": r.fraud
        }
        for r in records
    ]