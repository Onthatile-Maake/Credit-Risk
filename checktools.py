try:
    import fastapi
    import joblib
    from sklearn.ensemble import RandomForestClassifier
    print("✅ All systems go! FastAPI, Joblib, and Sklearn are working.")
except ImportError as e:
    print(f"❌ Still missing something: {e}")
