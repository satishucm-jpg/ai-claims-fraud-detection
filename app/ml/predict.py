import joblib
import numpy as np

# Load model
model = joblib.load("app/ml/model.pkl")

def predict_fraud(amount, age, claim_type):
    input_data = np.array([[amount, age, claim_type]])
    prediction = model.predict(input_data)
    return int(prediction[0])