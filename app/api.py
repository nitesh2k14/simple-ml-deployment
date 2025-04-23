
from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

class InputData(BaseModel):
    features: list

@app.post("/predict")
def get_prediction(input: InputData):
    prediction = predict(input.features)
    return {"prediction": prediction.tolist()}
