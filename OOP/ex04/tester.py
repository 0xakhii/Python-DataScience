"""Tester for exercise 04 (vector / vector calculator)."""

import io
from contextlib import redirect_stdout

from ft_calculator import calculator


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def captured(function, v1: list, v2: list) -> str:
    """Call a calculator function and return what it printed."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        function(v1, v2)
    return buffer.getvalue().strip()


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)
        print("=== additional checks ===")

        check("dotproduct", captured(calculator.dotproduct, a, b)
              == "Dot product is: 56")
        check("add_vec", captured(calculator.add_vec, a, b)
              == "Add Vector is : [7.0, 14.0, 5.0]")
        check("sous_vec", captured(calculator.sous_vec, a, b)
              == "Sous Vector is: [3.0, 6.0, -1.0]")

        # Floats
        check("dotproduct floats",
              captured(calculator.dotproduct, [0.5, 2.0], [4.0, 0.25])
              == "Dot product is: 2.5")
        check("add_vec floats",
              captured(calculator.add_vec, [0.5, 1.5], [0.5, 0.5])
              == "Add Vector is : [1.0, 2.0]")

        # Orthogonal vectors / zero vectors
        check("orthogonal vectors",
              captured(calculator.dotproduct, [1, 0], [0, 1])
              == "Dot product is: 0")
        check("zero vector",
              captured(calculator.add_vec, [0, 0], [0, 0])
              == "Add Vector is : [0.0, 0.0]")

        # Negative values
        check("negative values",
              captured(calculator.sous_vec, [-1, -2], [-3, 4])
              == "Sous Vector is: [2.0, -6.0]")

        # Inputs are not modified
        c, d = [1, 2, 3], [4, 5, 6]
        captured(calculator.add_vec, c, d)
        captured(calculator.sous_vec, c, d)
        check("inputs unchanged", c == [1, 2, 3] and d == [4, 5, 6])

        # Works without instantiation and through an instance
        check("via instance",
              captured(calculator().dotproduct, c, d)
              == "Dot product is: 32")

        # Docstrings
        check("class docstring", bool(calculator.__doc__))
        check("method docstrings",
              all([calculator.dotproduct.__doc__,
                   calculator.add_vec.__doc__,
                   calculator.sous_vec.__doc__]))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
