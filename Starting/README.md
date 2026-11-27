# Complete Guide to the Starting Folder (`ex00` – `ex09`)

> This guide explains every exercise in **Module 0 — Starting**, covering Python's core data structures, date/time formatting, runtime type and null checks, CLI argument parsing, regular expressions, functional helpers, dictionaries, generators, and modern Python packaging.

## Table of Contents

- [Directory Structure Overview](#directory-structure-overview)
- [Exercise 00 — Hello](#exercise-00--hello-built-in-collections--mutability)
- [Exercise 01 — format_ft_time](#exercise-01--format_ft_time-unix-epoch--date-formatting)
- [Exercise 02 — find_ft_type](#exercise-02--find_ft_type-runtime-type-inspection)
- [Exercise 03 — NULL_not_found](#exercise-03--null_not_found-null-falsy-values--nan)
- [Exercise 04 — whois](#exercise-04--whois-cli-arguments--parity-check)
- [Exercise 05 — building](#exercise-05--building-character-counting-with-regex--stdin)
- [Exercise 06 — ft_filter & filterstring](#exercise-06--ft_filter--filterstring-higher-order-filtering--lambdas)
- [Exercise 07 — sos](#exercise-07--sos-morse-code-encoding-with-dictionaries)
- [Exercise 08 — Loading](#exercise-08--loading-generators-yield--terminal-progress-bars)
- [Exercise 09 — ft_package](#exercise-09--ft_package-python-packaging-with-pyprojecttoml)
- [Reference](#reference-built-ins-keywords--stdlib-utilities)

## Directory Structure Overview

| Exercise | Files | Core concepts |
|:---|:---|:---|
| `ex00` | `Hello.py` | Built-in collections (`list`, `tuple`, `set`, `dict`), mutability vs. immutability |
| `ex01` | `format_ft_time.py` | `datetime` arithmetic, Unix epoch, `strftime`, `Decimal`, string formatting |
| `ex02` | `find_ft_type.py`, `tester.py` | `isinstance()`, `type()`, `__name__`, dynamic type dispatch |
| `ex03` | `NULL_not_found.py`, `tester.py` | `None`, `NaN` self-inequality, exact `type(x) is ...` checks, falsy values |
| `ex04` | `whois.py` | `sys.argv`, `sys.exit()`, exception handling (`AssertionError`, `ValueError`), modulo |
| `ex05` | `building.py` | Regular expressions (`re.findall`), `sys.stdin.read()`, `__name__ == "__main__"` |
| `ex06` | `ft_filter.py`, `filterstring.py` | Custom `filter` re-implementation, list comprehensions, `lambda`, string validation |
| `ex07` | `sos.py` | Dictionary lookup tables, generator expressions, `str.join()`, alphanumeric validation |
| `ex08` | `Loading.py`, `tester.py` | Generator functions (`yield`), `os.get_terminal_size()`, carriage-return rendering (`\r`) |
| `ex09` | `pyproject.toml`, `README.md`, `LICENSE`, `src/ft_package/`, `tester.py` | PEP 621 packaging, `src/` layout, `uv` workspace configuration, reusable package exports |

---

# Exercise 00 — `Hello`: Built-in Collections & Mutability

**Files:** `Hello.py`

## Concepts Explained

### Python's Four Core Collection Types

| Collection | Literal | Ordered | Mutable | Unique Elements |
|:---|:---|:---|:---|:---|
| `list` | `["Hello", "tata!"]` | Yes | Yes | No |
| `tuple` | `("Hello", "toto!")` | Yes | No | No |
| `set` | `{"Hello", "tutu!"}` | No | Yes | Yes |
| `dict` | `{"Hello": "titi!"}` | Insertion order (3.7+) | Yes | Keys are unique |

### Updating Each Collection

- **List:** Supports direct index assignment (`ft_list[1] = "World!"`).
- **Tuple:** Immutable, so modifying an element requires converting to a `list`, updating the element, and reconstructing a `tuple`:

  ```python
  lst = list(ft_tuple)
  lst[1] = "Morocco!"
  ft_tuple = tuple(lst)
  ```

- **Set:** Unindexed, so replacement uses `.discard()` (safe even if absent) followed by `.add()`.
- **Dictionary:** Updated in place via key assignment (`ft_dict["Hello"] = "1337!"`).

---

# Exercise 01 — `format_ft_time`: Unix Epoch & Date Formatting

**Files:** `format_ft_time.py`

## Concepts Explained

### Unix Epoch & `timedelta`

The Unix epoch is **January 1, 1970 (00:00:00)**. Subtracting two `datetime.datetime` objects produces a `datetime.timedelta`, whose `.total_seconds()` method converts the duration into floating-point seconds:

```python
epoch = dtm.datetime(1970, 1, 1)
seconds = (dtm.datetime(2026, 6, 23) - epoch).total_seconds()
```

### Number & Date Formatting

- **Thousands separator:** `f"{seconds:,}"` inserts commas every three digits.
- **Scientific notation:** `'%.2E' % dc.Decimal(seconds)` converts `seconds` to a `decimal.Decimal` and formats it with two decimal places in uppercase exponential notation.
- **Human-readable date:** `datetime.now().strftime("%b %d %Y")` formats the current date as abbreviated month, zero-padded day, and four-digit year (e.g., `Nov 27 2026`).

---

# Exercise 02 — `find_ft_type`: Runtime Type Inspection

**Files:** `find_ft_type.py` · `tester.py`

## Concepts Explained

### Everything Is an Object

In Python, every value is an instance of a class, accessible via `type(obj)`. Each type object exposes its class name through `type(obj).__name__` (e.g., `"list"`, `"tuple"`, `"set"`, `"dict"`).

### Branching on Type

- Strings receive a custom message (`"<name> is in the kitchen: <class 'str'>"`).
- Integers print `"Type not found"`.
- Other collection types capitalize their type name using `type(object).__name__.capitalize()`.

## Functions Breakdown

### `find_ft_type.py`

#### `all_thing_is_obj(object: any) -> int`

Inspects the runtime type of `object`, prints the corresponding formatted line, and always returns `42`.

### `tester.py`

Passes a `list`, `tuple`, `set`, `dict`, two `str` values (`"Brian"`, `"Toto"`), and an `int` (`10`), printing the return value `42` on the final call.

---

# Exercise 03 — `NULL_not_found`: Null, Falsy Values & `NaN`

**Files:** `NULL_not_found.py` · `tester.py`

## Concepts Explained

### Detecting `NaN` via IEEE 754 Self-Inequality

In IEEE 754 floating-point arithmetic, `NaN` (Not a Number) is the only value that is **not equal to itself**:

```python
type(object) is float and object != object
```

### Exact Type Checks (`type(x) is ...`) vs. `isinstance()`

Because `bool` is a subclass of `int` in Python (`isinstance(False, int)` is `True`), using `type(object) is bool` and `type(object) is int` cleanly distinguishes `False` (`Fake`) from `0` (`Zero`).

| Input | Condition | Output Label |
|:---|:---|:---|
| `None` | `object is None` | `Nothing:` |
| `float("NaN")` | `type(object) is float and object != object` | `Cheese:` |
| `False` | `type(object) is bool and not object` | `Fake:` |
| `0` | `type(object) is int and not object` | `Zero:` |
| `""` | `type(object) is str and not object` | `Empty:` |
| Anything else | `else` | `Type not Found` (returns `1`) |

> [!NOTE]
> **Return value tuple:** In `NULL_not_found.py`, the matched branches execute `return print(...), 0`, which evaluates `print(...)` (yielding `None`) and returns the tuple `(None, 0)`, whereas the unrecognized fallback prints `"Type not Found"` and returns `1`.

## Functions Breakdown

### `NULL_not_found.py`

#### `NULL_not_found(object: any) -> int`

Classifies null/falsy sentinel values and prints their label, value, and type; prints `"Type not Found"` and returns `1` for any non-null input.

### `tester.py`

Tests `None`, `float("NaN")`, `0`, `""`, `False`, and `"Brian"`, printing the return value for `"Brian"`.

---

# Exercise 04 — `whois`: CLI Arguments & Parity Check

**Files:** `whois.py`

## Concepts Explained

### Command-Line Arguments with `sys.argv`

`sys.argv` is a list of strings where `sys.argv[0]` is the script path and `sys.argv[1:]` are user-supplied arguments:

- `len(sys.argv) == 1`: exits quietly with `sys.exit(0)`.
- `len(sys.argv) > 2`: raises `AssertionError("AssertionError: more than one argument is provided")`.
- Non-integer `sys.argv[1]`: catches `ValueError` from `int()` and re-raises `AssertionError("AssertionError: argument is not an integer")`.

### Parity Determination

After converting negative integers to positive (`arg = arg * -1`), parity is tested with the modulo operator:

- `arg % 2 != 0` prints `"I'm Odd."`
- Otherwise prints `"I'm Even."` (including `0`).

---

# Exercise 05 — `building`: Character Counting with Regex & `stdin`

**Files:** `building.py`

## Concepts Explained

### Regular Expression Character Classes

`re.findall(pattern, text)` returns a list of every non-overlapping match in `text`, so `len(re.findall(...))` counts occurrences of each category:

| Category | Regex Pattern | Matches |
|:---|:---|:---|
| Uppercase letters | `([A-Z])` | ASCII `A`–`Z` |
| Lowercase letters | `([a-z])` | ASCII `a`–`z` |
| Punctuation marks | `r'[^\w\s]'` | Non-word, non-whitespace characters |
| Spaces | `r'\s'` | Spaces, tabs, newlines, and other whitespace |
| Digits | `([0-9])` | ASCII `0`–`9` |

### Fallback to Standard Input

When no CLI argument is supplied, `main()` prompts `"What is the text to count? "` with `flush=True` and reads all input from `sys.stdin.read()`.

## Functions Breakdown

### `building.py`

#### `building(input: str)`

Prints the total character count followed by the five category counts using `re.findall`.

#### `main()`

Validates `len(sys.argv) <= 2`, dispatches either `sys.argv[1]` or `sys.stdin.read()` to `building()`, and catches `AssertionError`.

---

# Exercise 06 — `ft_filter` & `filterstring`: Higher-Order Filtering & Lambdas

**Files:** `ft_filter.py` · `filterstring.py`

## Concepts Explained

### Re-implementing `filter()`

Python's built-in `filter(func, iterable)` selects elements for which `func(item)` evaluates to truthy. `ft_filter` illustrates the underlying loop mechanics by accumulating matching items into a new list.

### List Comprehensions & `lambda` Expressions

In `filterstring.py`, words are filtered in a single expression combining a list comprehension with an inline anonymous function (`lambda`):

```python
ret = [word for word in newList if (lambda w: len(w) >= length)(word)]
```

### Defensive Input Validation

Before filtering, `filterstring` verifies:

1. Exactly two CLI arguments are given (`len(sys.argv) == 3`).
2. Every character of `length` is numeric (`.isnumeric()`).
3. Every character of `input` is alphabetic or whitespace (`.isalpha() or .isspace()`).

Invalid inputs raise `AssertionError("AssertionError: the arguments are bad")`, print the message, and exit with status `1`.

## Functions Breakdown

### `ft_filter.py`

#### `ft_filter(func, iterable)`

Iterates over `iterable`, appends every element where `func(it)` is truthy to a list, and returns that list.

### `filterstring.py`

#### `filterstring(input, length)`

Validates `input` and `length`, splits `input` on `' '`, and returns all words satisfying `len(w) >= int(length)`.

#### `main()`

Checks argument count, calls `filterstring(str(sys.argv[1]), sys.argv[2])`, and prints the resulting list.

---

# Exercise 07 — `sos`: Morse Code Encoding with Dictionaries

**Files:** `sos.py`

## Concepts Explained

### Dictionary-Based Lookup Tables

`MORSE_CODE` maps uppercase characters to their Morse code strings in $O(1)$ average lookup time.

### Generator Expression with `str.join()`

Encoding is performed lazily across the input string:

```python
print(' '.join(MORSE_CODE.get(c.upper()) for c in input))
```

Each character is uppercased, looked up in `MORSE_CODE`, and joined with a single space.

> [!NOTE]
> **Character coverage in `ex07` vs. `ex09`:** `ex07/sos.py` defines entries for `A`–`Z` and `0`–`5` (while validating `isalnum() or isspace()`). In `ex09/src/ft_package/ft_package.py`, `MORSE_CODE` is expanded to also include digits `6`–`9` and `' ': '/'`.

## Functions Breakdown

### `sos.py`

#### `morse_encode(input)`

Validates that all characters are alphanumeric or whitespace, encodes each character via `MORSE_CODE`, and prints the space-separated Morse string.

#### `main()`

Ensures `len(sys.argv) == 2`, invokes `morse_encode(str(sys.argv[1]))`, and handles `AssertionError` with exit code `1`.

---

# Exercise 08 — `Loading`: Generators, `yield` & Terminal Progress Bars

**Files:** `Loading.py` · `tester.py`

## Concepts Explained

### Generators & `yield`

Unlike a regular function that computes and returns an entire collection at once, a generator function containing `yield` suspends its execution state on each iteration and resumes where it left off on the next call to `next()`. This allows `ft_tqdm(range(333))` to wrap any `range` with $O(1)$ extra memory.

### Dynamic In-Place Terminal Rendering

1. **Terminal width:** `os.get_terminal_size().columns` queries the active TTY width, falling back to `80` columns if stdout is not attached to a terminal (`OSError`).
2. **Progress calculation:** For 1-based index $i$ out of $N = \text{total}$:

   $$
   \text{percentage} = \left\lfloor \frac{100 \cdot i}{N} \right\rfloor, \qquad
   \text{filled} = \left\lfloor \frac{\text{bar\_size} \cdot i}{N} \right\rfloor
   $$

3. **In-place overwrite:** Printing `\r` moves the cursor back to column 0 without advancing to a new line (`end=''`), and `flush=True` forces immediate rendering on each step.

## Functions Breakdown

### `Loading.py`

#### `ft_tqdm(lst: range) -> None`

Iterates over `lst` with `enumerate(lst, start=1)`, draws a `'█'` progress bar sized to the terminal width, prints `percentage%|bar| i/total` in place, and `yield`s each item. Returns immediately if `len(lst) == 0`.

### `tester.py`

Runs `tqdm(range(333))` followed by `ft_tqdm(range(333))` with `sleep(0.005)` per step for side-by-side visual comparison.

---

# Exercise 09 — `ft_package`: Python Packaging with `pyproject.toml`

**Files:** `pyproject.toml` · `README.md` · `LICENSE` · `src/ft_package/__init__.py` · `src/ft_package/ft_package.py` · `tester.py`

## Concepts Explained

### PEP 621 & the `src/` Layout

Modern Python packages declare their metadata in `pyproject.toml` rather than legacy `setup.py` scripts:

- `[project]`: package name (`ft_package`), version (`0.0.1`), author, description, `requires-python = ">=3.9"`, classifiers, and `MIT` license.
- `src/ft_package/`: isolates importable package code from project root scripts so tests run against the installed package.
- `[tool.uv.workspace]`, `[tool.uv.sources]`, and `[dependency-groups]`: configure local workspace installation for `uv`.

## Package Contents Breakdown

### `src/ft_package/ft_package.py`

Consolidates three reusable utilities from earlier exercises:

- `filterstring(input, length)` — word-length filter from `ex06`.
- `morse_encode(input)` — Morse code encoder from `ex07`, extended with digits `6`–`9` and `' ': '/'`.
- `ft_tqdm(lst: range)` — generator progress bar from `ex08`.

### `tester.py`

Imports `ft_tqdm` and `morse_encode` from `ft_package`, animates a 222-step progress bar, and encodes `"Don3"` into Morse code.

---

# Reference: Built-ins, Keywords & Stdlib Utilities

| Symbol | Category | Purpose in Starting |
|:---|:---|:---|
| `list`, `tuple`, `set`, `dict` | Built-in types | Core mutable and immutable data structures (`ex00`, `ex02`, `ex07`) |
| `isinstance()`, `type()` | Built-ins | Runtime type inspection and exact-type comparison (`ex02`, `ex03`) |
| `len()`, `int()`, `str()`, `float()` | Built-ins | Length measurement and explicit type conversion (`ex03`–`ex08`) |
| `enumerate()`, `max()` | Built-ins | 1-based indexed iteration and minimum progress-bar width clamping (`ex08`) |
| `yield`, `lambda` | Keywords | Lazy generator production and inline predicates (`ex06`, `ex08`, `ex09`) |
| `try` / `except` / `raise` | Error handling | Catching `AssertionError`, `ValueError`, and `OSError` (`ex04`–`ex09`) |
| `datetime`, `strftime`, `Decimal` | `datetime` / `decimal` | Epoch seconds calculation, date formatting, scientific notation (`ex01`) |
| `sys.argv`, `sys.stdin`, `sys.exit()` | `sys` module | CLI argument parsing, piped input reading, exit codes (`ex04`–`ex07`) |
| `re.findall()` | `re` module | Counting uppercase, lowercase, punctuation, spaces, and digits (`ex05`) |
| `os.get_terminal_size()` | `os` module | Adapting progress bar width to the terminal window (`ex08`, `ex09`) |
| `time.sleep()` | `time` module | Simulating work in progress-bar testers (`ex08`, `ex09`) |
| `pyproject.toml` | Packaging (PEP 621) | Declarative package metadata and `uv` workspace config (`ex09`) |
