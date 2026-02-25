from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title="SA Credit Risk API")

# Load our saved brain
model = joblib.load('model/credit_model.pkl')

@app.get("/")
def home():
    return {"message": "The Credit Risk API is Live and Running!"}

@app.post("/predict")
def predict(income: int, score: int):
    # Convert input into a format the model understands
    input_df = pd.DataFrame([[income, score]], columns=['income_pm', 'credit_score'])
    prediction = model.predict(input_df)[0]
    
    result = "Approved" if prediction == 1 else "Declined"
    return {
        "monthly_income": income,
        "credit_score": score,
        "decision": result
    }