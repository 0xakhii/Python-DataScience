"""Tester for exercise 03 (new_student dataclass)."""

import inspect
import string
from dataclasses import is_dataclass

from new_student import Student, generate_id


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        print("---")
        try:
            Student(name="Edward", surname="agle", id="toto")
            check("id is not initializable", False)
        except TypeError as error:
            print(f"TypeError: {error}")
            check("id is not initializable", True)

        print("=== additional checks ===")

        # Dataclass structure and no custom __str__ / __repr__
        src = inspect.getsource(Student)
        check("Student is a dataclass", is_dataclass(Student))
        check("no custom __str__ defined", "def __str__" not in src)
        check("no custom __repr__ defined", "def __repr__" not in src)

        # Field values
        check("name stored", student.name == "Edward")
        check("surname stored", student.surname == "agle")
        check("active defaults to True", student.active is True)
        check("login computed as 'Eagle'", student.login == "Eagle")
        check("id length is 15", len(student.id) == 15)
        check("id is all lowercase ascii",
              all(ch in string.ascii_lowercase for ch in student.id))

        # Repr format matches subject
        expected_repr = (
            f"Student(name='Edward', surname='agle', active=True, "
            f"login='Eagle', id='{student.id}')"
        )
        check("repr matches subject format", repr(student) == expected_repr)

        # login must also not be initializable
        try:
            Student(name="Edward", surname="agle", login="Eagle")
            check("login is not initializable", False)
        except TypeError:
            check("login is not initializable", True)

        # active can be overridden and IDs are unique per instance
        inactive = Student(name="alice", surname="Smith", active=False)
        check("active=False respected", inactive.active is False)
        check("login normalizes case", inactive.login == "Asmith")
        check("unique random IDs per instance", student.id != inactive.id)

        # Empty name edge case handled safely
        empty = Student(name="", surname="solo")
        check("empty name does not raise IndexError", empty.login == "solo")

        # Docstrings
        check("all docstrings present",
              all([generate_id.__doc__, Student.__doc__,
                   Student.__post_init__.__doc__]))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
