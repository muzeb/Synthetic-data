from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model and preprocessing objects
model = joblib.load('../../pipeline/deploy/classical-ai/rf_classifier_model.pkl')
label_encoders = joblib.load('../../pipeline/deploy/classical-ai/rf_label_encoders.pkl')
scaler = joblib.load('../../pipeline/deploy/classical-ai/rf_scaler.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define the input data model
class InputData(BaseModel):
    src_bytes: float
    dst_bytes: float
    count: float
    serror_rate: float
    protocol: int
    service: int

# Prediction endpoint
@app.post("/predict")
def predict(data: InputData):
    # Create an array with the input features
    #input_array = np.array([[data.src_bytes, data.dst_bytes, data.count, data.serror_rate]])
    input_array = np.array([[data.src_bytes, data.dst_bytes, data.count, data.serror_rate, data.protocol, data.service]])
    
    # Scale the numerical features (first 4 columns)
    input_array[:, :4] = scaler.transform(input_array[:, :4])
    
    # Predict using the model
    prediction = model.predict(input_array)
    
    # Return the prediction result
    return {"prediction": "normal" if prediction[0] == 0 else "attack"}

# Run the FastAPI app using uvicorn (in terminal): uvicorn app:app --reload
