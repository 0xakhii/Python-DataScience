import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
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

def main():
    family = [[1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))

if __name__ == "__main__":
    main()