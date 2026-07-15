import cv2


def load_image(file_path: str):
    """
    Load an image from disk using OpenCV.

    Args:
        file_path (str): Path of the uploaded image.

    Returns:
        numpy.ndarray | None:
            Returns the loaded image if successful,
            otherwise None.
    """

    image = cv2.imread(file_path)

    return image





def preprocess_image(image):
    """
    Convert the image to grayscale.
    More preprocessing steps can be added later.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray