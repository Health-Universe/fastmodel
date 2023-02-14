from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World"}

@app.post("/compute")
def compute(x: float, y: float):
    return {"result": x + y}
