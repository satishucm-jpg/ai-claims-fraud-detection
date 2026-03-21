from fastapi import FastAPI
from pydantic import BaseModel
from app.ml.predict import predict_fraud

app = FastAPI()

class Claim(BaseModel):
    amount: float
    age: int
    claim_type: int

@app.get("/")
def home():
    return {"message": "AI Fraud Detection API Running 🚀"}

@app.post("/predict")
def predict(claim: Claim):
    result = predict_fraud(claim.amount, claim.age, claim.claim_type)
    return {"fraud": result}