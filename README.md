# ai-claims-fraud-detection
AI-powered fraud detection system using FastAPI, Machine Learning, and scalable backend architecture
📌 Overview

This project is a production-ready AI-powered fraud detection system built using FastAPI and Machine Learning.
It predicts whether an insurance claim is fraudulent based on claim amount, customer age, and claim type.
The system supports real-time prediction and stores results for historical analysis.

🧠 Features
	•	Real-time fraud prediction using ML model
	•	REST API built with FastAPI
	•	Modular backend architecture (API, services, schemas)
	•	Logging for monitoring requests and predictions
	•	SQLite database for storing prediction history
	•	Swagger UI for API testing
	•	Historical data retrieval via API

⚙️ Tech Stack
	•	Python
	•	FastAPI
	•	Scikit-learn
	•	Pandas
	•	SQLAlchemy
	•	SQLite
	•	Uvicorn


📂 Project Structure
app/
├── api/            # API routes
├── services/       # Business logic
├── schemas/        # Request validation
├── core/           # Config & logging
├── db/             # Database models & setup
├── ml/             # ML model & training
├── main.py         # Entry point

🔹 Health Check

GET /

🔹 Predict Fraud

POST /predict

Example Request:{
  "amount": 5000,
  "age": 45,
  "claim_type": 1
}
Example Response: {
  "fraud": 1
}

💼 Use Case

This system can be used by insurance companies to:
	•	Detect fraudulent claims in real-time
	•	Analyze historical fraud patterns
	•	Improve operational efficiency
  
  👨‍💻 Author: Sai Satish
