import pandas as pd
from importlib import import_module
import joblib
from sklearn.ensemble import RandomForestClassifier
import os

# Create folders if they don't exist
os.makedirs('model', exist_ok=True)

# 1. Create a tiny South African dataset (Income in Rand, Credit Score)
data = {
    'income_pm': [5000, 12000, 45000, 8000, 55000, 15000],
    'credit_score': [400, 550, 750, 420, 800, 600],
    'loan_approved': [0, 1, 1, 0, 1, 1] # 0 = Declined, 1 = Approved
}
df = pd.DataFrame(data)

# 2. Train the model
X = df[['income_pm', 'credit_score']]
y = df['loan_approved']
model = RandomForestClassifier(n_estimators=10)
model.fit(X, y)

# 3. Save the model to the 'model/' folder
joblib.dump(model, 'model/credit_model.pkl')
print("✅ Success: Model trained and saved in /model folder!")