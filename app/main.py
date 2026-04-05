from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello, FastAPI!",
        "timestamp": datetime.now()
    }

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/env")
def read_env():
    return {
        "app_env": os.getenv("APP_ENV", "not set")
    }