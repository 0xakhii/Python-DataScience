"""Module providing a decorator factory that limits function calls."""

from typing import Any


def callLimit(limit: int):
    """Return a decorator that allows a function to be called at most limit."""
    count = 0

    def callLimiter(function):
        """Wrap the target function with call-count enforcement."""
        def limit_function(*args: Any, **kwds: Any):
            """Invoke function if count < limit, otherwise print an error."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")
            return None

        return limit_function

    return callLimiter


def main() -> None:
    """Run a brief standalone smoke check for callLimit."""
    @callLimit(1)
    def sample() -> None:
        """Sample decorated function."""
        print("sample()")

    sample()
    sample()


if __name__ == "__main__":
    main()
