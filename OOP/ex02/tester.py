"""Tester for exercise 02 (DiamondTrap)."""

from DiamondTrap import King
from S1E7 import Baratheon, Lannister
from S1E9 import Character


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)
        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)
        print("=== additional checks ===")

        # Inheritance and C3 linearization
        check("King is a Baratheon", isinstance(Joffrey, Baratheon))
        check("King is a Lannister", isinstance(Joffrey, Lannister))
        check("King is a Character", isinstance(Joffrey, Character))
        check("MRO is C3 linearized",
              King.__mro__ == (King, Baratheon, Lannister,
                               Character, Character.__mro__[1],
                               object))

        # Default values
        Tommen = King("Tommen")
        check("default family_name", Tommen.family_name == "Baratheon")
        check("default eyes", Tommen.get_eyes() == "brown")
        check("default hairs", Tommen.get_hairs() == "dark")
        check("default is_alive", Tommen.is_alive is True)

        # Getters / setters
        Tommen.set_eyes("green")
        check("set_eyes", Tommen.get_eyes() == "green")
        check("set_eyes keeps __dict__ in sync",
              Tommen.__dict__["eyes"] == "green")
        Tommen.set_hairs("red")
        check("set_hairs", Tommen.get_hairs() == "red")

        # Properties
        Tommen.eyes = "grey"
        check("property setter", Tommen.get_eyes() == "grey")
        check("property getter", Tommen.hairs == "red")

        # Instances are independent
        check("other king untouched", Joffrey.get_eyes() == "blue")

        # Inherited behaviour
        Tommen.die()
        check("die() inherited", Tommen.is_alive is False)
        check("str() inherited",
              str(Tommen) == "Vector: ('Baratheon', 'grey', 'red')")

        # Docstrings
        check("class docstring", bool(King.__doc__))
        check("method docstrings",
              all([King.get_eyes.__doc__, King.set_eyes.__doc__,
                   King.get_hairs.__doc__, King.set_hairs.__doc__]))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
