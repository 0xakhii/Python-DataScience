import numpy as np
import cv2 as cv

def ft_load(path: str) -> array:
    try:
        img = cv.imread(path)
        if not path.endswith((".jpg", ".jpeg", ".png")):
            raise FileExistsError("File format not supported")
        if img is None:
            raise FileNotFoundError()
        width, height, classes = img.shape
        # print(f"The shape of image is: ({width}, {height}, {classes})")
        img_rgb = img[:, :, ::-1]
        # print(img_rgb)
    except FileNotFoundError:
        return
    except FileExistsError as error:
        print(error)
        return
    return img_rgb
