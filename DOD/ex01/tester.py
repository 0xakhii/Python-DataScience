"""Tester for exercise 01 (in_out)."""

from in_out import outer, pow, square


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
        print("=== additional checks ===")

        # Direct function checks
        check("square(4) == 16", square(4) == 16)
        check("square(-2.5) == 6.25", square(-2.5) == 6.25)
        check("pow(3) == 27", pow(3) == 27)
        check("pow(2) == 4", pow(2) == 4)

        # Subject sequence checks
        c1 = outer(3, square)
        check("square seq [9, 81, 6561]",
              [c1(), c1(), c1()] == [9, 81, 6561])

        c2 = outer(1.5, pow)
        results = [c2(), c2(), c2()]
        expected = [1.8371173070873836, 3.056683336818703, 30.42684786675409]
        check("pow seq matches subject", results == expected)

        # Independent closures & custom functions
        c_a = outer(2, square)
        c_b = outer(2, square)
        check("c_a first call == 4", c_a() == 4)
        check("c_a second call == 16", c_a() == 16)
        check("c_b stays independent (== 4)", c_b() == 4)

        inc = outer(0, lambda n: n + 1)
        check("custom function closure", [inc(), inc(), inc()] == [1, 2, 3])
        check("outer returns a callable", callable(inc))

        # Docstrings
        check("all docstrings present",
              all([square.__doc__, pow.__doc__, outer.__doc__, inc.__doc__]))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
