"""Module to load an image and display its information."""

import os
import cv2 as cv
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """Loads an image from path, prints its format and pixels in RGB,

    and returns it as a NumPy array.

    Args:
        path (str): The path to the image file to load.

    Returns:
        np.ndarray | None: RGB image pixel array, or None if an error occurs.
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("Path must be a string.")
        if not os.path.exists(path):
            raise FileNotFoundError("File not found. Check the provided path")
        if not path.lower().endswith((".jpg", ".jpeg", ".png")):
            raise FileExistsError("File format not supported")
        img = cv.imread(path)
        if img is None:
            raise ValueError("Failed to decode image file.")
        width, height, classes = img.shape
        print(f"The shape of image is: ({width}, {height}, {classes})")
        img_rgb = img[:, :, ::-1]
        print(img_rgb)
        return img_rgb
    except FileNotFoundError as error:
        print(f"FileNotFoundError: {error}")
        return None
    except FileExistsError as error:
        print(f"FileExistsError: {error}")
        return None
    except Exception as error:
        print(f"Error: {error}")
        return None
