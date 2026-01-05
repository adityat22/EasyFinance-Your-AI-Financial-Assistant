import os
import logging

# Suppress TensorFlow and other logs
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
logging.getLogger('tensorflow').setLevel(logging.ERROR)

from fastapi import FastAPI
from fastapi.responses import FileResponse
from config import settings
from src.api import endpoints

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    print("\n" + "="*50)
    print(f"Server is running at: http://127.0.0.1:8001/")
    print("="*50 + "\n")

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

app.include_router(endpoints.router, prefix=settings.API_V1_STR)

@app.get("/")
def root():
    return FileResponse(os.path.join(static_dir, "login.html"))

@app.get("/chat")
def chat_page():
    return FileResponse(os.path.join(static_dir, "index.html"))
