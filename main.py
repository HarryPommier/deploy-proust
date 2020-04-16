from fastapi import FastAPI
from pydantic import BaseModel
from ml.model import model as proust_model


app = FastAPI()

class PredictRequest(BaseModel):
    data: str

class PredictResponse(BaseModel):
    data: str

@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest):
    output_text = proust_model.generate_text(input.data)
    return PredictResponse(data=output_text)
