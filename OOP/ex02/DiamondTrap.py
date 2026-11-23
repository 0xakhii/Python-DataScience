"""Module defining the King, a Baratheon/Lannister diamond inheritance."""

from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King, heir of both Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a King (MRO: King, Baratheon, Lannister, Character)."""
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        """Return the eyes color of the King."""
        return self.__dict__["eyes"]

    def set_eyes(self, color: str) -> None:
        """Set the eyes color of the King."""
        self.__dict__["eyes"] = color

    def get_hairs(self) -> str:
        """Return the hairs color of the King."""
        return self.__dict__["hairs"]

    def set_hairs(self, color: str) -> None:
        """Set the hairs color of the King."""
        self.__dict__["hairs"] = color

    eyes = property(get_eyes, set_eyes, doc="Eyes color of the King.")
    hairs = property(get_hairs, set_hairs, doc="Hairs color of the King.")
