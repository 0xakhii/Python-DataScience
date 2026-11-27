"""Module providing math operations and a stateful closure wrapper."""


def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure that iteratively applies function starting from x."""
    count = 0

    def inner() -> float:
        """Apply function to the current state, increment count, and return."""
        nonlocal count, x
        count += 1
        x = function(x)
        return x

    return inner


def main() -> None:
    """Run a brief standalone smoke check for outer, square, and pow."""
    counter = outer(3, square)
    print(counter())


if __name__ == "__main__":
    main()
