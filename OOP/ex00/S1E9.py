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
