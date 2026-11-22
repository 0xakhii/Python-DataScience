"""Module to zoom and rotate an image using matrix transposition."""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom(path: str) -> np.ndarray | None:
    """Loads an image from path and slices a zoomed square region.

    Args:
        path (str): The path to the image file.

    Returns:
        np.ndarray | None: The cropped image as a NumPy array, or None.
    """
    img = ft_load(path)
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cropped = gray[100:500, 450:850]
    cropped = cropped[:, :, np.newaxis]
    return cropped


def rotate(path: str) -> None:
    """Rotates the zoomed image using matrix transposition and displays it.

    Args:
        path (str): The path to the image file to rotate.
    """
    cropped = zoom(path)
    if cropped is None:
        return
    print(f"The shape of image is: ({cropped.shape})")
    print(cropped)
    rows, cols = cropped.shape[:2]
    transposed = np.zeros((cols, rows, 3), dtype=cropped.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed[j, i] = cropped[i, j]
    print(f"New shape after Transpose: {transposed.shape}")
    print(transposed)
    plt.imshow(transposed, cmap="gray")
    plt.xticks(np.arange(0, 351, 50))
    plt.yticks(np.arange(0, 351, 50))
    plt.show()


def main() -> None:
    """Main function to rotate and display the animal image."""
    rotate("/home/ojamal/Downloads/animal.jpeg")


if __name__ == "__main__":
    main()
