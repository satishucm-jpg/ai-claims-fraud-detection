import joblib
import pandas as pd
from app.core.logger import logger

model = joblib.load("app/ml/model.pkl")

def predict_fraud(amount, age, claim_type):
    logger.info(f"Incoming request → amount={amount}, age={age}, type={claim_type}")

    input_data = pd.DataFrame([{
        "amount": amount,
        "age": age,
        "claim_type": claim_type
    }])

    prediction = model.predict(input_data)

    logger.info(f"Prediction result → {prediction[0]}")

    return int(prediction[0])