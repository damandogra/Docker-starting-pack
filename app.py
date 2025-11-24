from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello from docker", "env": os.getenv("ENV", "local")}