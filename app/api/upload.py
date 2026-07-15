from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.ocr_service import load_image

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_image(image: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_DIR,
        image.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Load image using OpenCV
    loaded_image = load_image(file_path)

    # Validate image
    if loaded_image is None:
        return {
            "message": "Failed to load image."
        }

    return {
        "message": "Image uploaded successfully.",
        "filename": image.filename,
        "status": "Image loaded successfully."
    }
