from fastapi import APIRouter, UploadFile, File
import os
import shutil

from app.services.ocr_service import (
    load_image,
    preprocess_image
)

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

    loaded_image = load_image(file_path)

    if loaded_image is None:
        return {
            "message": "Failed to load image."
        }

    processed_image = preprocess_image(loaded_image)

    return {
        "message": "Image uploaded successfully.",
        "filename": image.filename,
        "image_shape": list(processed_image.shape)
    }
