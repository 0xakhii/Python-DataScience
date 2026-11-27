"""Tester for exercise 02 (callLimit)."""

import io
from contextlib import redirect_stdout

from callLimit import callLimit


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        @callLimit(3)
        def f():
            """Print f()."""
            print("f()")

        @callLimit(1)
        def g():
            """Print g()."""
            print("g()")

        for _ in range(3):
            f()
            g()

        print("=== additional checks ===")

        # Verify return value forwarding and argument passing
        @callLimit(2)
        def add(a: int, b: int = 0) -> int:
            """Return sum of two integers."""
            return a + b

        check("1st call forwards args & return", add(2, 3) == 5)
        check("2nd call forwards kwargs & return", add(10, b=5) == 15)

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            blocked = add(1, 1)
        out = buffer.getvalue().strip()
        check("3rd call blocked returns None", blocked is None)
        check("3rd call prints expected error format",
              out.startswith("Error: <function ")
              and out.endswith(" call too many times"))

        # Limit of 0 blocks even the first call
        @callLimit(0)
        def never_runs() -> str:
            """Should never execute."""
            return "ran"

        buffer = io.StringIO()
        with redirect_stdout(buffer):
            res = never_runs()
        check("limit=0 blocks immediately",
              res is None and "call too many times" in buffer.getvalue())

        # Independent counters per decorated function
        @callLimit(1)
        def h1() -> str:
            """First independent function."""
            return "h1"

        @callLimit(1)
        def h2() -> str:
            """Second independent function."""
            return "h2"

        check("h1 runs once", h1() == "h1")
        check("h2 counter is independent", h2() == "h2")

        # Docstrings
        check("callLimit docstring present", bool(callLimit.__doc__))
        check("wrapper docstring present", bool(f.__doc__))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
