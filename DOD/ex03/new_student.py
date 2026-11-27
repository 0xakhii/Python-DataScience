"""Module defining the Student dataclass with auto-generated login and id."""

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Return a random 15-character lowercase alphabetic student ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Dataclass representing a student with computed login and random ID."""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self) -> None:
        """Compute the student login from name and surname."""
        self.login = self.name[:1].upper() + self.surname.lower()


def main() -> None:
    """Run a brief standalone smoke check for Student."""
    student = Student(name="Edward", surname="agle")
    print(student)


if __name__ == "__main__":
    main()
