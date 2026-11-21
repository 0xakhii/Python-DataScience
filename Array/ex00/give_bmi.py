def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi = []
    try:
        if len(height) != len(weight):
            raise AssertionError("AssertionError: Incomplete arguments")
        for i in range(len(height)):
            try:
                assert int(height[i])
                assert float(height[i])
            except ValueError:
                print("ValueError: Given values are neither int nor float")
                return []
            if weight[i] < 0 or height[i] < 0:
                raise AssertionError("AssertionError: Cannot accept negative values")
            bmi.append(weight[i] / (height[i] * height[i]))
    except AssertionError as error:
        print(error)
        return []
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    is_limit = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            is_limit.append(True)
        else:
            is_limit.append(False)
    return is_limit

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
if __name__ == "__main__":
    main()