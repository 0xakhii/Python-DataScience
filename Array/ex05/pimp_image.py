"""Apply color filters to RGB images and display the results."""

import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def _prepare(array: np.ndarray) -> np.ndarray | None:
    """Validate an RGB array and return an independent copy.

    Args:
        array (np.ndarray): The image array to validate and copy.

    Returns:
        np.ndarray | None: A copy of the RGB image, or None if invalid.
    """
    if not isinstance(array, np.ndarray):
        return None
    if array.ndim != 3 or array.shape[2] != 3:
        return None
    result = array.copy()
    return result


def _show(array: np.ndarray, title: str) -> np.ndarray:
    """Print and display an RGB image.

    Args:
        array (np.ndarray): The filtered image array to print and display.
        title (str): The title of the displayed image window.

    Returns:
        np.ndarray: The displayed image array.
    """
    print(f"The shape of image is: {array.shape}")
    print(array)
    plt.figure()
    plt.title(title)
    plt.imshow(array)
    plt.axis("off")
    plt.show()
    return array


def ft_invert(array) -> np.ndarray:
    """Inverts the colors of the received RGB image.

    Args:
        array (np.ndarray): The RGB image array to invert.

    Returns:
        np.ndarray: A copy of the inverted image.
    """
    result = _prepare(array)
    if result is None:
        return array
    result = 255 - result
    return _show(result, "Invert")


def ft_red(array) -> np.ndarray:
    """Keeps only the red channel of the received RGB image.

    Args:
        array (np.ndarray): The RGB image array to filter.

    Returns:
        np.ndarray: A copy containing only the red channel.
    """
    result = _prepare(array)
    if result is None:
        return array
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    return _show(result, "Red")


def ft_green(array) -> np.ndarray:
    """Keeps only the green channel of the received RGB image.

    Args:
        array (np.ndarray): The RGB image array to filter.

    Returns:
        np.ndarray: A copy containing only the green channel.
    """
    result = _prepare(array)
    if result is None:
        return array
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return _show(result, "Green")


def ft_blue(array) -> np.ndarray:
    """Keeps only the blue channel of the received RGB image.

    Args:
        array (np.ndarray): The RGB image array to filter.

    Returns:
        np.ndarray: A copy containing only the blue channel.
    """
    result = _prepare(array)
    if result is None:
        return array
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return _show(result, "Blue")


def ft_grey(array) -> np.ndarray:
    """Converts the received RGB image to grayscale.

    Args:
        array (np.ndarray): The RGB image array to convert.

    Returns:
        np.ndarray: A copy of the grayscale image with three channels.
    """
    result = _prepare(array)
    if result is None:
        return array
    grey = result.astype(np.float32)
    grey = grey.mean(axis=2, keepdims=True)
    grey = grey / 1
    result = np.repeat(grey.astype(np.uint8), 3, axis=2)
    return _show(result, "Grey")


def main() -> None:
    """Load the landscape image and display each color filter."""
    array = ft_load("/home/ojamal/Downloads/landscape.jpg")
    _show(array, "Original")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
