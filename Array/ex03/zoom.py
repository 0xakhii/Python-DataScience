"""Module to load an image, zoom (slice) a region, and display it."""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(path: str = "animal.jpeg") -> np.ndarray | None:
    """Loads an image, slices a 400x400 region, prints its new shape

    and pixel content, and displays it with axis scales.

    Args:
        path (str): Path to the image file. Defaults to 'animal.jpeg'.

    Returns:
        np.ndarray | None: Sliced image as a NumPy array, or None on failure.
    """
    try:
        img = ft_load(path)
        if img is None:
            return None

        if img.shape[0] < 500 or img.shape[1] < 850:
            raise AssertionError("Image dimensions are too small for slicing.")

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        cropped = gray[100:500, 450:850]
        cropped = cropped[:, :, np.newaxis]

        print(f"New shape after slicing: {cropped.shape}")
        print(cropped)

        plt.imshow(cropped.squeeze(), cmap="gray")
        plt.xticks(np.arange(0, 351, 50))
        plt.yticks(np.arange(0, 351, 50))
        plt.show()

        return cropped
    except Exception as error:
        print(f"Error: {error}")
        return None


def main():
    """Main program entry point to run zoom on animal.jpeg."""
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
