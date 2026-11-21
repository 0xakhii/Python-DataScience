from load_image import ft_load
import cv2 as cv2
import numpy as np
import matplotlib.pyplot as plt

def zoom(path: str):
    img = ft_load(path)
    print(f"The shape of image: ({img.shape[0]}, {img.shape[1]}, {img.shape[2]})\n{img}")

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cropped = gray[100:500, 450:850]
    cropped = cropped[:, :, np.newaxis]

    print(f"New shape after slicing: {cropped.shape} or {cropped.shape[:2]}")
    print(cropped)

    plt.imshow(cropped.squeeze(), cmap="gray")
    plt.xticks(np.arange(0, 351, 50))
    plt.yticks(np.arange(0, 351, 50))
    plt.show()
    
    return cropped

def main():
    zoom("/home/akhi/Downloads/animal.jpeg")

if __name__ == "__main__":
    main()
