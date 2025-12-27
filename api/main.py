from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
 
app=FastAPI(title="Diabetes Prediction API")

model=joblib.load("../model/diabetes_model.pkl")

class PatientData(BaseModel):
    age:int
    hypertension:float
    heart_disease:bool
    bmi:float
    HbA1c_level:float
    blood_glucose_level:int

@app.get("/")
def home():
    return {'Message':"Diabetes Prediction API"}

@app.post("/predict")
def predict(data: PatientData):
    input_data=np.array([[
        data.age,
        data.hypertension,
        data.heart_disease,
        data.bmi,
        data.HbA1c_level,
        data.blood_glucose_level

    ]])
    prediction=model.predict(input_data)[0]
    return{
        "Prediction":int(prediction),
        "result":"Diabetic" if prediction ==1 else "Not Diabetic"


    }
