from fastapi import FastAPI

app = FastAPI(
    title="PAN OCR API",
    description="Production-ready PAN OCR API using FastAPI and PaddleOCR",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "PAN OCR API is running successfully."
    }
