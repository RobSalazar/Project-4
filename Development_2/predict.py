import joblib

rf_model = joblib.load("../ml_models/rf_model.joblib")

def predictor(features):
    return rf_model.predict(features)