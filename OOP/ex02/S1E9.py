"""Module defining the abstract Character class and the Stark family."""

from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class representing a character."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a character with a first name and a health state."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Change the health state of the character from alive to dead."""
        self.is_alive = False


class Stark(Character):
    """Representing the Stark family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Stark character."""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Make the Stark character die."""
        super().die()


def main() -> None:
    """Run a small demonstration of the Character and Stark classes."""
    try:
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive)
        Ned.die()
        print(Ned.is_alive)
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)
        print("---")
        Character("hodor")
    except TypeError as error:
        print(f"TypeError: {error}")


if __name__ == "__main__":
    main()
