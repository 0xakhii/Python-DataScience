"""Module defining the Baratheon and Lannister families."""

from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Baratheon character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Make the Baratheon character die."""
        self.is_alive = False

    def __str__(self) -> str:
        """Return the family traits as a string."""
        return (f"Vector: ('{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """Return the family traits as a string."""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Lannister character."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """Make the Lannister character die."""
        self.is_alive = False

    def __str__(self) -> str:
        """Return the family traits as a string."""
        return (f"Vector: ('{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """Return the family traits as a string."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> "Lannister":
        """Create a Lannister character without calling the constructor."""
        return cls(first_name, is_alive)


def main() -> None:
    """Run the subject demonstration of the Baratheon and Lannister."""
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive)
        Robert.die()
        print(Robert.is_alive)
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive)
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__}, "
              f"Alive : {Jaine.is_alive}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
