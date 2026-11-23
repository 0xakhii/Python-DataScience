"""Tester for exercise 00 (S1E9)."""

from S1E9 import Character, Stark


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def main() -> None:
    """Run the subject tester followed by additional checks."""
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
        print("=== additional checks ===")

        # Abstract class cannot be instantiated
        try:
            Character("hodor")
            check("Character is abstract", False)
        except TypeError as error:
            print(f"TypeError: {error}")
            check("Character is abstract", True)

        # Default values and inheritance
        Arya = Stark("Arya")
        check("is_alive defaults to True", Arya.is_alive is True)
        check("Stark inherits from Character", isinstance(Arya, Character))
        check("first_name is stored", Arya.first_name == "Arya")

        # die() flips the state, and is idempotent
        Arya.die()
        check("die() sets is_alive to False", Arya.is_alive is False)
        Arya.die()
        check("die() twice stays False", Arya.is_alive is False)

        # Instances are independent
        Sansa = Stark("Sansa")
        check("instances are independent", Sansa.is_alive is True)

        # Explicit is_alive value
        check("is_alive=False respected", Lyanna.is_alive is False)

        # Docstrings
        check("class has a docstring", bool(Stark.__doc__))
        check("Character has a docstring", bool(Character.__doc__))
        check("constructor has a docstring", bool(Stark.__init__.__doc__))
        check("method has a docstring", bool(Stark.die.__doc__))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
