from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get("/")

def getName():
    return {"Hello": "World"}