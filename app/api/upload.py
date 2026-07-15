from fastapi import APIRouter, UploadFile, File
import os
import shutil

router = APIRouter()

UPLOAD_DIR = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    """
    Upload an image and save it to the uploads folder.
    """

    file_path = os.path.join(UPLOAD_DIR, image.filename)

    # Save the uploaded image
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "message": "Image uploaded successfully.",
        "filename": image.filename
    }