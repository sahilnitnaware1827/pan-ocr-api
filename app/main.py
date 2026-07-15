from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="PAN OCR API",
    description="Production-ready PAN OCR API using FastAPI",
    version="1.0.0"
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "PAN OCR API is running successfully."
    }
