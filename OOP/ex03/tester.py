"""Tester for exercise 03 (vector / scalar calculator)."""

import io
from contextlib import redirect_stdout

from ft_calculator import calculator


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def captured(vector: list[float], operation: str, scalar: float) -> tuple:
    """Apply an operation, returning the printed output and the vector."""
    calc = calculator(vector)
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        if operation == "+":
            calc + scalar
        elif operation == "*":
            calc * scalar
        elif operation == "-":
            calc - scalar
        else:
            calc / scalar
    return buffer.getvalue().strip(), calc.vector


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
        print("=== additional checks ===")

        out, vec = captured([0.0, 1.0, 2.0], "+", 5)
        check("addition", vec == [5.0, 6.0, 7.0])
        check("addition output", out == "[5.0, 6.0, 7.0]")

        out, vec = captured([0.0, 1.0, 2.0], "*", 5)
        check("multiplication", vec == [0.0, 5.0, 10.0])

        out, vec = captured([10.0, 15.0, 20.0], "-", 5)
        check("subtraction", vec == [5.0, 10.0, 15.0])

        out, vec = captured([10.0, 15.0, 20.0], "/", 5)
        check("division", vec == [2.0, 3.0, 4.0])

        out, vec = captured([1.0, 2.0], "+", -3)
        check("negative scalar", vec == [-2.0, -1.0])

        out, vec = captured([1.0, 2.0], "*", 0)
        check("multiply by zero", vec == [0.0, 0.0])

        out, vec = captured([1.0, 2.0], "*", 0.5)
        check("float scalar", vec == [0.5, 1.0])

        out, vec = captured([], "+", 5)
        check("empty vector", vec == [] and out == "[]")

        out, vec = captured([1, 2, 3], "+", 1)
        check("ints converted to floats",
              all(isinstance(x, float) for x in vec))

        out, vec = captured([1.0, 2.0], "/", 0)
        check("division by zero handled", vec == [1.0, 2.0])
        check("division by zero message", "ZeroDivisionError" in out)

        # Chained operations on the same instance
        calc = calculator([1.0, 2.0])
        with redirect_stdout(io.StringIO()):
            calc + 1
            calc * 2
        check("operations accumulate", calc.vector == [4.0, 6.0])

        # Docstrings
        check("class docstring", bool(calculator.__doc__))
        check("method docstrings",
              all([calculator.__add__.__doc__, calculator.__mul__.__doc__,
                   calculator.__sub__.__doc__,
                   calculator.__truediv__.__doc__]))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
