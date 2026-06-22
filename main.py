from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def hello():
    return "Hello World"
@app.get("/welcome")
def welcome():
    return "Welcome to FastAPI"
@app.get("/greet/{name}")
def greet(name:str):
    return f"Hello {name}, welcome to FastAPI"
    