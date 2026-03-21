import joblib
import pandas as pd
from app.core.logger import logger
from app.db.database import SessionLocal
from app.db.models import ClaimRecord

model = joblib.load("app/ml/model.pkl")

def predict_fraud(amount, age, claim_type):
    logger.info(f"Incoming request → amount={amount}, age={age}, type={claim_type}")

    input_data = pd.DataFrame([{
        "amount": amount,
        "age": age,
        "claim_type": claim_type
    }])

    prediction = model.predict(input_data)
    result = int(prediction[0])

    # 🔥 Save to DB
    db = SessionLocal()
    record = ClaimRecord(
        amount=amount,
        age=age,
        claim_type=claim_type,
        fraud=result
    )
    db.add(record)
    db.commit()
    db.close()

    logger.info(f"Prediction saved to DB → {result}")

    return result