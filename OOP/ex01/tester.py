"""Tester for exercise 01 (S1E7)."""

from S1E7 import Baratheon, Lannister
from S1E9 import Character


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def main() -> None:
    """Run the subject tester followed by additional checks."""
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
        print("=== additional checks ===")

        # Inheritance
        check("Baratheon is a Character", isinstance(Robert, Character))
        check("Lannister is a Character", isinstance(Cersei, Character))

        # Attributes
        check("Baratheon traits",
              (Robert.family_name, Robert.eyes, Robert.hairs)
              == ("Baratheon", "brown", "dark"))
        check("Lannister traits",
              (Cersei.family_name, Cersei.eyes, Cersei.hairs)
              == ("Lannister", "blue", "light"))

        # __str__ and __repr__ return real strings
        check("str() returns a str", isinstance(str(Robert), str))
        check("repr() returns a str", isinstance(repr(Cersei), str))
        check("str() content",
              str(Robert) == "Vector: ('Baratheon', 'brown', 'dark')")
        check("repr() content",
              repr(Cersei) == "Vector: ('Lannister', 'blue', 'light')")

        # die()
        Tywin = Lannister("Tywin")
        check("Lannister alive by default", Tywin.is_alive is True)
        Tywin.die()
        check("Lannister die()", Tywin.is_alive is False)

        # Class method
        check("create_lannister type", type(Jaine) is Lannister)
        Dead = Lannister.create_lannister("Joffrey", False)
        check("create_lannister is_alive=False", Dead.is_alive is False)
        Default = Lannister.create_lannister("Tyrion")
        check("create_lannister default alive", Default.is_alive is True)
        check("create_lannister traits", Default.eyes == "blue")

        # Character stays abstract
        try:
            Character("hodor")
            check("Character is abstract", False)
        except TypeError:
            check("Character is abstract", True)

        # Docstrings
        check("Baratheon docstring", bool(Baratheon.__doc__))
        check("Lannister docstring", bool(Lannister.__doc__))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
