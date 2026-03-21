import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Dummy dataset (simple example)
data = pd.DataFrame({
    "amount": [100, 5000, 200, 7000],
    "age": [25, 45, 30, 50],
    "claim_type": [0, 1, 0, 1],
    "fraud": [0, 1, 0, 1]
})

# Features and target
X = data[["amount", "age", "claim_type"]]
y = data["fraud"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "app/ml/model.pkl")

print("Model trained and saved!")