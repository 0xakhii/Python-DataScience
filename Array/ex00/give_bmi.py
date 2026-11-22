"""Module for calculating Body Mass Index (BMI) and applying limits."""


def give_bmi(
        height: list[int | float],
        weight: list[int | float]) -> list[int | float]:
    """Calculate the BMI (Body Mass Index) from height and weight lists.

    Args:
        height (list[int | float]): Heights of persons in meters.
        weight (list[int | float]): Weights of persons in kilograms.

    Returns:
        list[int | float]: Calculated BMI values for each person.

    Raises:
        AssertionError: If list lengths differ or values are negative.
    """
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
                ErrMsg = "AssertionError: Cannot accept negative values"
                raise AssertionError(ErrMsg)
            bmi.append(weight[i] / (height[i] * height[i]))
    except AssertionError as error:
        print(error)
        return []
    return bmi


def apply_limit(
        bmi: list[int | float],
        limit: int) -> list[bool]:
    """Applies a limit threshold to BMI values.

    Args:
        bmi (list[int | float]): List of calculated BMI values.
        limit (int): Threshold limit to compare against.

    Returns:
        list[bool]: List of booleans (True if BMI > limit, else False).
    """
    is_limit = []
    for i in range(len(bmi)):
        if bmi[i] > limit:
            is_limit.append(True)
        else:
            is_limit.append(False)
    return is_limit


# def main():
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]
#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))


# if __name__ == "__main__":
#     main()
