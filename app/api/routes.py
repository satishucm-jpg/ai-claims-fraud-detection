from fastapi import APIRouter
from app.schemas.claim_schema import Claim
from app.services.prediction_service import predict_fraud

router = APIRouter()

@router.get("/")
def home():
    return {"message": "AI Fraud Detection API Running 🚀"}

@router.post("/predict")
def predict(claim: Claim):
    result = predict_fraud(claim.amount, claim.age, claim.claim_type)
    return {"fraud": result}