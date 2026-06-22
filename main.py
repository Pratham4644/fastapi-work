from fastapi import FastAPI
from pydantic import BaseModel


class PredictRequest(BaseModel):
    text: str


app = FastAPI(title="FastAPI ML/AI Journey")


@app.get("/")
def hello():
    return {"message": "Hello World from FastAPI"}


@app.get("/welcome")
def welcome():
    return {"message": "Welcome to FastAPI"}


@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}, welcome to FastAPI"}


@app.post("/predict")
def predict(request: PredictRequest):
    return {
        "prediction": f"Received text with {len(request.text)} characters",
        "input": request.text,
    }
