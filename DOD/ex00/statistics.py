"""Module providing basic descriptive statistics over variable arguments."""

from typing import Any


def _compute_mean(values: list[int | float]) -> float:
    """Return the arithmetic mean of a non-empty list of numbers."""
    return sum(values) / len(values)


def _compute_median(sorted_values: list[int | float]) -> int | float:
    """Return the median of a non-empty sorted list of numbers."""
    length = len(sorted_values)
    mid = length // 2
    if length % 2 == 1:
        return sorted_values[mid]
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2


def _compute_quartile(sorted_values: list[int | float]) -> list[float]:
    """Return the 25% and 75% quartiles using linear interpolation."""
    length = len(sorted_values)
    quartiles = []
    for percentile in (0.25, 0.75):
        pos = percentile * (length - 1)
        low = int(pos)
        high = low + 1 if low + 1 < length else low
        frac = pos - low
        value = sorted_values[low] + frac * (
            sorted_values[high] - sorted_values[low]
        )
        quartiles.append(float(value))
    return quartiles


def _compute_variance(values: list[int | float]) -> float:
    """Return the population variance of a non-empty list of numbers."""
    mean = _compute_mean(values)
    return sum((x - mean) ** 2 for x in values) / len(values)


def _compute_std(values: list[int | float]) -> float:
    """Return the population standard deviation of a non-empty list."""
    return _compute_variance(values) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Compute and print requested statistics for the numeric arguments."""
    try:
        valid_ops = {"mean", "median", "quartile", "std", "var"}
        valid_numbers = bool(args) and all(
            isinstance(x, (int, float)) and not isinstance(x, bool)
            for x in args
        )
        values = list(args) if valid_numbers else []
        sorted_values = sorted(values) if valid_numbers else []

        for operation in kwargs.values():
            if not isinstance(operation, str) or operation not in valid_ops:
                continue
            if not valid_numbers:
                print("ERROR")
                continue
            if operation == "mean":
                print(f"mean : {_compute_mean(values)}")
            elif operation == "median":
                print(f"median : {_compute_median(sorted_values)}")
            elif operation == "quartile":
                print(f"quartile : {_compute_quartile(sorted_values)}")
            elif operation == "std":
                print(f"std : {_compute_std(values)}")
            elif operation == "var":
                print(f"var : {_compute_variance(values)}")
    except Exception:
        print("ERROR")


def main() -> None:
    """Run a brief standalone smoke check for ft_statistics."""
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                  tata="quartile")


if __name__ == "__main__":
    main()
