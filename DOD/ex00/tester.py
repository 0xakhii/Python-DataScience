"""Tester for exercise 00 (ft_statistics)."""

import io
from contextlib import redirect_stdout

from statistics import ft_statistics


def check(label: str, condition: bool) -> None:
    """Print a PASS/FAIL line for a given condition."""
    print(f"[{'PASS' if condition else 'FAIL'}] {label}")


def captured(*args, **kwargs) -> str:
    """Call ft_statistics and return its captured stdout."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        ft_statistics(*args, **kwargs)
    return buffer.getvalue().strip()


def main() -> None:
    """Run the subject tester followed by additional checks."""
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median",
                      tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                      world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                      ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
        print("=== additional checks ===")

        # Subject exact output checks
        out = captured(1, 42, 360, 11, 64, toto="mean", tutu="median",
                       tata="quartile")
        expected = "mean : 95.6\nmedian : 42\nquartile : [11.0, 64.0]"
        check("subject mean/median/quartile", out == expected)

        out = captured(5, 75, 450, 18, 597, 27474, 48575, hello="std",
                       world="var")
        expected = "std : 17982.70124086944\nvar : 323377543.9183673"
        check("subject std/var", out == expected)

        out = captured(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh",
                       ejdjdejn="kdekem")
        check("unknown kwargs produce no output", out == "")

        out = captured(toto="mean", tutu="median", tata="quartile")
        check("empty args print ERROR per request",
              out == "ERROR\nERROR\nERROR")

        # Edge cases
        check("even length median",
              captured(1, 2, 3, 4, a="median") == "median : 2.5")
        check("single value all stats",
              captured(10, a="mean", b="median", c="quartile", d="var",
                       e="std")
              == ("mean : 10.0\nmedian : 10\nquartile : [10.0, 10.0]\n"
                  "var : 0.0\nstd : 0.0"))
        check("negative numbers",
              captured(-10, 0, 10, a="mean", b="median")
              == "mean : 0.0\nmedian : 0")
        check("non-numeric args print ERROR",
              captured(1, "bad", 3, a="mean") == "ERROR")
        check("boolean args rejected as non-numeric",
              captured(True, False, a="mean") == "ERROR")
        check("no args and no kwargs", captured() == "")
        check("docstring present", bool(ft_statistics.__doc__))
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
