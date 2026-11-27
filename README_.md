# Complete Guide to the DOD Folder (`ex00` – `ex03`)

> This guide explains every exercise in **Module 4 — Data Oriented Design (DOD)**, covering the underlying Python design concepts, mathematical formulas, execution flows, functions, methods, decorators, and standard-library utilities used.

## Table of Contents

- [Directory Structure Overview](#directory-structure-overview)
- [Exercise 00 — Statistics](#exercise-00--statistics-variadic-arguments--descriptive-statistics)
- [Exercise 01 — Closures](#exercise-01--in_out-closures--nonlocal)
- [Exercise 02 — Call Limits](#exercise-02--calllimit-decorator-factories--wrappers)
- [Exercise 03 — Dataclasses](#exercise-03--new_student-dataclasses-field--__post_init__)
- [Reference](#reference-built-ins-keywords--stdlib-utilities)

## Directory Structure Overview

| Exercise | Files | Core concepts |
|:---|:---|:---|
| `ex00` | `statistics.py`, `tester.py` | Variadic `*args` and `**kwargs`, descriptive statistics, defensive numeric validation, error handling |
| `ex01` | `in_out.py`, `tester.py` | First-class and higher-order functions, nested functions, closures, LEGB scope, `nonlocal` |
| `ex02` | `callLimit.py`, `tester.py` | Decorator factories, nested wrappers, argument forwarding, per-function closure state |
| `ex03` | `new_student.py`, `tester.py` | `@dataclass`, generated methods, `field()`, `default_factory`, `__post_init__` |

---

# Exercise 00 — `statistics`: Variadic Arguments & Descriptive Statistics

**Files:** `statistics.py` · `tester.py`

## Concepts Explained

### Variadic Parameters: `*args` and `**kwargs`

- `*args` packs positional arguments into a tuple:

  ```python
  (1, 42, 360, 11, 64)
  ```

- `**kwargs` packs keyword arguments into a dictionary:

  ```python
  {'toto': 'mean', 'tutu': 'median', 'tata': 'quartile'}
  ```

  Dictionary insertion order is preserved in Python 3.7+.

- In `ft_statistics`, keyword names such as `toto`, `hello`, and `world` are arbitrary.
- Only `kwargs.values()` determines which statistics to print.
- Unknown values such as `"heheh"` are silently ignored.

### Numeric Validation & the Boolean-as-Integer Pitfall

In Python, `bool` is a subclass of `int`:

```python
isinstance(True, int)  # True
```

The implementation therefore explicitly uses:

```python
isinstance(x, (int, float)) and not isinstance(x, bool)
```

This rejects booleans instead of silently treating `True` and `False` as `1` and `0`.

## Descriptive Statistics Formulas

Given $N$ numeric observations:

$$
x_0, x_1, \ldots, x_{N-1}
$$

sorted as:

$$
s_0 \leq s_1 \leq \cdots \leq s_{N-1}
$$

### Mean

$$
\mu = \frac{1}{N}\sum_{i=0}^{N-1} x_i
$$

### Median

- **Odd $N$:** the middle element

  $$
s_{\lfloor N/2 \rfloor}
  $$

- **Even $N$:** the average of the two central elements

  $$
  \frac{s_{N/2-1}+s_{N/2}}{2}
  $$

### Quartiles

The implementation uses linear interpolation matching the default behavior of `numpy.percentile`.

For $p \in \{0.25, 0.75\}$:

$$
pos = p \cdot (N-1)
$$

$$
low = \lfloor pos \rfloor
$$

$$
high = \min(low+1, N-1)
$$

$$
frac = pos-low
$$

$$
Q_p = s_{low} + frac \cdot (s_{high}-s_{low})
$$

For `[1, 11, 42, 64, 360]`, where $N=5$:

- $pos_{0.25}=1.0 \Rightarrow Q_1=11.0$
- $pos_{0.75}=3.0 \Rightarrow Q_3=64.0$

### Population Variance

$$
\sigma^2 = \frac{1}{N}\sum_{i=0}^{N-1}(x_i-\mu)^2
$$

### Population Standard Deviation

$$
\sigma = \sqrt{\sigma^2} = (\sigma^2)^{0.5}
$$

> [!NOTE]
> **Module shadowing — `statistics.py` vs. the standard-library `statistics` module**
>
> Python's standard library includes a module named `statistics`. When running:
>
> ```bash
> python3 DOD/ex00/tester.py
> ```
>
> Python puts `DOD/ex00/` first in `sys.path[0]`. Consequently:
>
> ```python
> from statistics import ft_statistics
> ```
>
> loads the local `statistics.py` instead of the standard-library module.

## Functions Breakdown

### `statistics.py`

#### `_compute_mean(values: list[int | float]) -> float`

Computes:

```python
sum(values) / len(values)
```

#### `_compute_median(sorted_values: list[int | float]) -> int | float`

- Returns the middle item for odd-length lists, preserving the integer type for integer inputs.
- For an odd-length list, this matches `median : 42`.
- Returns the average of the two central items for even-length lists.

#### `_compute_quartile(sorted_values: list[int | float]) -> list[float]`

Computes `[Q1, Q3]` as a two-element list of floats using linear interpolation.

It safely handles single-element lists with:

```python
low + 1 < length
```

#### `_compute_variance(values: list[int | float]) -> float`

Uses a generator expression:

```python
sum((x - mean) ** 2 for x in values) / len(values)
```

This computes population variance.

#### `_compute_std(values: list[int | float]) -> float`

Computes:

```python
_compute_variance(values) ** 0.5
```

It does not need `math.sqrt`, respecting **Allowed functions: None**.

#### `ft_statistics(*args: Any, **kwargs: Any) -> None`

- Validates `*args`.
- Sorts once if the arguments are valid.
- Loops through `kwargs.values()`.
- Ignores unknown operation strings.
- Prints `ERROR` for each valid operation when `*args` is empty or invalid.
- Wraps everything in `try/except Exception` so no error escapes uncaught.

#### `main() -> None`

Guarded smoke check under:

```python
if __name__ == "__main__":
```

### `tester.py`

#### `check(label, condition)`

Checks the supplied condition and associates it with a label.

#### `captured(*args, **kwargs)`

- Redirects standard output into an `io.StringIO` buffer.
- Uses `contextlib.redirect_stdout` to capture exact printed output.
- Tests subject cases and edge cases:
  - even lengths;
  - single values;
  - negatives;
  - non-numbers;
  - booleans.

---

# Exercise 01 — `in_out`: Closures & `nonlocal`

**Files:** `in_out.py` · `tester.py`

## Concepts Explained

### First-Class & Higher-Order Functions

In Python, functions are objects just like numbers or lists:

- They can be passed as arguments:

  ```python
  outer(3, square)
  ```

- They can be returned from other functions:

  ```python
  return inner
  ```

A function that takes or returns another function is called a **higher-order function**.

### Lexical Scope: The LEGB Rule

Python resolves variable names in this order:

```text
Local → Enclosing → Global → Built-in
```

### Closures

When `outer()` returns `inner`, the `outer()` stack frame finishes, but `inner` retains references to the enclosing variables `x`, `count`, and `function` inside closure cells (`inner.__closure__`).

Every call to `outer(...)` creates a brand-new set of closure cells:

```python
my_counter = outer(3, square)
another_counter = outer(1.5, pow)
```

Therefore, `my_counter` and `another_counter` keep completely independent state without using global variables.

### Why `nonlocal` Is Required

Inside `inner()`:

- Reading an enclosing variable works automatically.
- Assigning to it, such as `count += 1` or `x = function(x)`, makes Python treat the variable as a new local variable.
- This can cause an `UnboundLocalError`.

```python
nonlocal count, x
```

This tells Python to rebind existing variables in the nearest enclosing function scope (`outer`) rather than creating local shadows or modifying module globals.

## Execution Trace

### `my_counter = outer(3, square)`

| Call | State before call | Result |
|---:|:---|---:|
| 1 | `count = 1`, `x = square(3) = 9` | `9` |
| 2 | `count = 2`, `x = square(9) = 81` | `81` |
| 3 | `count = 3`, `x = square(81) = 6561` | `6561` |

### `another_counter = outer(1.5, pow)`

| Call | Calculation | Result |
|---:|:---|---:|
| 1 | $1.5^{1.5}$ | `1.8371173070873836` |
| 2 | $1.8371173070873836^{1.8371173070873836}$ | `3.056683336818703` |
| 3 | $3.056683336818703^{3.056683336818703}$ | `30.42684786675409` |

## Functions Breakdown

### `in_out.py`

#### `square(x: int | float) -> int | float`

Returns:

```python
x * x
```

It preserves `int` for integer inputs and `float` for floating-point inputs.

#### `pow(x: int | float) -> int | float`

Returns:

```python
x ** x
```

This is self-exponentiation. Defining `pow` here creates a module-level function that shadows the built-in `pow`, as required by the subject prototype.

#### `outer(x: int | float, function) -> object`

- Initializes `count = 0`.
- Defines the nested `inner` function.
- Returns the `inner` function object without invoking it.

#### `inner() -> float`

- Uses `nonlocal count, x`.
- Increments `count`.
- Updates `x = function(x)` in $O(1)$ per call.
- Returns the new value of `x`.

---

# Exercise 02 — `callLimit`: Decorator Factories & Wrappers

**Files:** `callLimit.py` · `tester.py`

## Concepts Explained

### Decorators vs. Decorator Factories

A plain decorator such as `@dec`:

1. Takes a function.
2. Returns a replacement function.

It is a two-layer structure.

Because `@callLimit(3)` accepts a parameter, it requires a **decorator factory** with three nested functions:

```python
@callLimit(3)
def f():
    print("f()")
```

is 100% equivalent to:

```python
def f():
    print("f()")

f = callLimit(3)(f)
```

### Nested Structure

```text
callLimit(limit)
└── callLimiter(function)
    └── limit_function(*args, **kwds)
```

### Transparent Argument & Return Forwarding

`limit_function(*args: Any, **kwds: Any)` allows `@callLimit(...)` to wrap functions with any signature:

- `f()` — no arguments;
- `add(10, b=5)` — positional and keyword arguments.

When allowed, the wrapper returns:

```python
function(*args, **kwds)
```

This preserves the wrapped function's return value. When blocked, it returns `None`.

### Closure Isolation Across Decorated Functions

Each `@callLimit(...)` decoration invokes `callLimit` separately, allocating its own `count = 0` closure cell.

Therefore:

- `f`, with a limit of `3`, tracks its own call count.
- `g`, with a limit of `1`, tracks a separate call count.

## Functions Breakdown

### `callLimit.py`

#### `callLimit(limit: int)`

- The outer decorator factory.
- Stores `limit`.
- Initializes `count = 0`.
- Returns `callLimiter`.

#### `callLimiter(function)`

- The actual decorator receiving the target function.
- Returns the wrapper `limit_function`.

#### `limit_function(*args: Any, **kwds: Any)`

- Uses `nonlocal count`.
- Checks whether `count < limit`.
- If under the limit:
  - increments `count`;
  - calls and returns `function(*args, **kwds)`.
- Otherwise prints:

  ```text
  Error: {function} call too many times
  ```

  where `{function}` formats as:

  ```text
  <function g at 0x...>
  ```

- Returns `None` when blocked.

---

# Exercise 03 — `new_student`: Dataclasses, `field()`, & `__post_init__`

**Files:** `new_student.py` · `tester.py`

## Concepts Explained

### What `@dataclass` Generates Automatically

Decorating `Student` with `@dataclass` inspects its type-annotated class attributes and generates boilerplate special methods.

#### Generated `__init__`

Only fields with `init=True` are included:

```python
Student(name: str, surname: str, active: bool = True)
```

#### Generated `__repr__`

The default `repr=True` setting displays every field in declaration order:

```python
Student(name='Edward', surname='agle', active=True,
        login='Eagle', id='...')
```

#### Generated `__eq__`

Fields are compared structurally for equality.

Because `__repr__` is generated automatically, `Student` satisfies the constraint:

> You must not use `__str__` or `__repr__` in your class.

## Controlling Fields with `dataclasses.field()`

### `active: bool = field(default=True)`

- Included in `__init__`.
- Defaults to `True`.
- Callers may omit it or override it:

  ```python
  Student(..., active=False)
  ```

### `login: str = field(init=False)`

- Excluded from `__init__` parameters.
- Passing `login=...` raises:

  ```text
  TypeError: Student.__init__() got an unexpected keyword argument 'login'
  ```

- The field is still included in `__repr__`.

### `id: str = field(init=False, default_factory=generate_id)`

- Excluded from `__init__`.
- Calls `generate_id()` fresh for every new instance.

## `default_factory` vs. `default`

```python
default=generate_id()
```

calls `generate_id()` once when the class is defined. Every `Student` instance would then share the exact same ID.

```python
default_factory=generate_id
```

passes the function reference instead. Python invokes it dynamically during each instantiation, giving every student a unique random ID.

## The `__post_init__` Lifecycle Hook

`login` depends on `self.name` and `self.surname`, so it cannot be computed using a zero-argument `default_factory`.

The dataclass-generated `__init__` therefore calls `__post_init__` immediately after assigning all initialized fields.

## Functions & Class Breakdown

### `new_student.py`

#### `generate_id() -> str`

- Calls:

  ```python
  random.choices(string.ascii_lowercase, k=15)
  ```

- Samples 15 lowercase letters with replacement.
- Concatenates the result with `"".join(...)`.

#### `Student`

Decorated with `@dataclass`, declaring:

- `name`;
- `surname`;
- `active`;
- `login`, with `init=False`;
- `id`, with `init=False` and `default_factory=generate_id`.

#### `Student.__post_init__(self) -> None`

Computes:

```python
self.login = self.name[:1].upper() + self.surname.lower()
```

Using `[:1]` instead of `[0]` avoids `IndexError` when `name` is an empty string.

### `tester.py`

The tester verifies:

- the subject output;
- `TypeError` when attempting to pass `id` or `login`;
- `dataclasses.is_dataclass(Student)`;
- absence of manually defined `__str__` or `__repr__` using `inspect.getsource(Student)`;
- random ID length;
- random ID character set;
- random ID uniqueness;
- `active=False` overrides;
- empty-name safety;
- required docstrings.

---

# Reference: Built-ins, Keywords & Stdlib Utilities

| Symbol | Category | Purpose in DOD |
|:---|:---|:---|
| `*args`, `**kwargs` | Python syntax | Capture positional tuples and keyword dictionaries (`ex00`, `ex02`) |
| `nonlocal` | Keyword | Rebind variables in an enclosing function scope (`ex01`, `ex02`) |
| `typing.Any` | Typing module | Represent an unconstrained dynamic type (`ex00`, `ex02`) |
| `sum()`, `len()`, `sorted()` | Built-ins | Aggregate totals, measure lengths, and create non-mutating sorted copies (`ex00`) |
| `isinstance()`, `all()`, `bool()` | Built-ins | Perform type validation and boolean assertion checks (`ex00`–`ex03`) |
| `callable()` | Built-in | Verify that `outer()` returns an invocable object (`ex01/tester.py`) |
| `@dataclass`, `field()` | `dataclasses` | Generate `__init__`, `__repr__`, and `__eq__`; configure field behavior (`ex03`) |
| `is_dataclass()` | `dataclasses` | Confirm at runtime that `Student` is a dataclass (`ex03/tester.py`) |
| `random.choices(..., k=15)` | `random` module | Draw 15 random elements with replacement (`ex03`) |
| `string.ascii_lowercase` | `string` module | Provide `'abcdefghijklmnopqrstuvwxyz'` (`ex03`) |
| `str.join()`, `upper()`, `lower()` | String methods | Build the 15-character ID and normalized login (`ex03`) |
| `io.StringIO`, `redirect_stdout` | `io` / `contextlib` | Capture printed output in memory (`ex00`, `ex02`) |
| `inspect.getsource()` | `inspect` module | Verify that `Student` has no custom `__str__` or `__repr__` (`ex03/tester.py`) |
