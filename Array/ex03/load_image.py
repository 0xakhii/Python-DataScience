"""Module to load an image and display its information."""

import os
import cv2 as cv
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """Loads an image from path, prints its format and pixels,

    and returns it as an RGB NumPy array.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray | None: The loaded image as an RGB NumPy array,
                           or None if loading fails.
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("Path must be a string.")
        if not os.path.exists(path):
            raise FileNotFoundError(f"No such file or directory: '{path}'")
        if not path.lower().endswith((".jpg", ".jpeg", ".png")):
            raise ValueError("File format not supported.")

        img = cv.imread(path)
        if img is None:
            raise ValueError("Failed to decode image file.")

        img_rgb = img[:, :, ::-1]
        print(f"The shape of image is: {img_rgb.shape}")
        print(img_rgb)
        return img_rgb
    except FileNotFoundError as error:
        print(f"FileNotFoundError: {error}")
        return None
    except Exception as error:
        print(f"Error: {error}")
        return None
