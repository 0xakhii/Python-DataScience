"""Module providing a vector / scalar calculator."""


class calculator:
    """Calculator applying scalar operations to a vector, in place."""

    def __init__(self, vector: list[float]) -> None:
        """Initialize the calculator with a vector of floats."""
        self.vector = [float(x) for x in vector]

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector and print it."""
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar and print it."""
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector and print it."""
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar and print it."""
        try:
            if object == 0:
                raise ZeroDivisionError("division by zero is not allowed")
            for i in range(len(self.vector)):
                self.vector[i] /= object
            print(self.vector)
        except ZeroDivisionError as error:
            print(f"ZeroDivisionError: {error}")
