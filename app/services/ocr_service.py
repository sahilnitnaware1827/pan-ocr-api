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
