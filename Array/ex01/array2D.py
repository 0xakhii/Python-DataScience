"""Module for 2D array slicing and shape inspection."""

import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Takes a 2D array, prints its shape, slices it, and prints the new shape.

    Args:
        family (list): A 2D list representing rows and columns.
        start (int): Starting index for slicing.
        end (int): Ending index for slicing.

    Returns:
        list: Sliced version of the 2D list.

    Raises:
        ValueError: If family is not a list or indices are out of range.
    """
    try:
        if type(family) is not list:
            raise ValueError("ValueError: argument is not list")
        if len(family) <= abs(start) or len(family) <= abs(end):
            raise ValueError("ValueError: indexes out of range")
        npArr = np.array(family)
        print("My shape is:", npArr.shape)
        newArr = []
        i = abs(start)
        while i < abs(end):
            newArr.append(family[i])
            i += 1
        npnewArr = np.array(newArr)
        print("My new shape is:", npnewArr.shape)
        return newArr
    except ValueError as error:
        print(error)
        return []
