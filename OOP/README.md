# Complete Guide to the OOP Folder (`ex00` – `ex04`)

> This guide explains every exercise in **Module 3 — Object-Oriented Programming (OOP)**, covering abstract base classes, inheritance, custom string representations, `@classmethod` factory constructors, diamond multiple inheritance and C3 linearization (MRO), `property` descriptors, arithmetic operator overloading, and `@staticmethod` vector math.

## Table of Contents

- [Directory Structure Overview](#directory-structure-overview)
- [Exercise 00 — S1E9](#exercise-00--s1e9-abstract-base-classes--single-inheritance)
- [Exercise 01 — S1E7](#exercise-01--s1e7-__str__-__repr__--classmethod)
- [Exercise 02 — DiamondTrap](#exercise-02--diamondtrap-multiple-inheritance-mro--properties)
- [Exercise 03 — ft_calculator (Scalar)](#exercise-03--ft_calculator-scalar-operator-overloading)
- [Exercise 04 — ft_calculator (Vector)](#exercise-04--ft_calculator-vector-staticmethod--vector-algebra)
- [Reference](#reference-built-ins-decorators--dunder-methods)

## Directory Structure Overview

| Exercise | Files | Core concepts |
|:---|:---|:---|
| `ex00` | `S1E9.py`, `tester.py` | `abc.ABC`, `@abstractmethod`, `super()`, abstract instantiation `TypeError` |
| `ex01` | `S1E9.py`, `S1E7.py`, `tester.py` | Concrete subclasses (`Baratheon`, `Lannister`), `__str__`, `__repr__`, `@classmethod` factory |
| `ex02` | `S1E9.py`, `S1E7.py`, `DiamondTrap.py`, `tester.py` | Diamond multiple inheritance, C3 Linearization (`__mro__`), `property()`, `__dict__` backing |
| `ex03` | `ft_calculator.py`, `tester.py` | Operator overloading (`__add__`, `__mul__`, `__sub__`, `__truediv__`), in-place mutation, `ZeroDivisionError` |
| `ex04` | `ft_calculator.py`, `tester.py` | `@staticmethod`, class-level vector operations (dot product, element-wise sum & difference) |

---

# Exercise 00 — `S1E9`: Abstract Base Classes & Single Inheritance

**Files:** `S1E9.py` · `tester.py`

## Concepts Explained

### Abstract Base Classes (`abc.ABC` & `@abstractmethod`)

Inheriting from `abc.ABC` and marking at least one method with `@abstractmethod` prevents direct instantiation of the base class:

```python
Character("hodor")
# TypeError: Can't instantiate abstract class Character ...
```

Subclasses must override every abstract method before they can be instantiated. Even though `Character.die()` is abstract, it still provides a reusable body (`self.is_alive = False`) that subclasses can invoke via `super().die()`.

### Delegating with `super()`

`Stark` inherits from `Character` and delegates both initialization and state transition to its superclass:

```python
super().__init__(first_name, is_alive)
super().die()
```

## Functions & Class Breakdown

### `S1E9.py`

#### `Character(ABC)`

- `__init__(self, first_name: str, is_alive: bool = True) -> None` — stores `self.first_name` and `self.is_alive` (defaults to `True`).
- `die(self) -> None` (`@abstractmethod`) — sets `self.is_alive = False`.

#### `Stark(Character)`

- `__init__(self, first_name: str, is_alive: bool = True) -> None` — delegates to `super().__init__`.
- `die(self) -> None` — implements the abstract method by calling `super().die()`.

### `tester.py`

Verifies subject output, `TypeError` when instantiating `Character`, default `is_alive=True`, explicit `is_alive=False`, idempotency of calling `die()` twice, instance independence, and docstrings.

---

# Exercise 01 — `S1E7`: `__str__`, `__repr__` & `@classmethod`

**Files:** `S1E9.py` · `S1E7.py` · `tester.py`

## Concepts Explained

### Customizing String Representation: `__str__` vs. `__repr__`

- `__str__(self)` defines the user-friendly string returned by `str(obj)` and `print(obj)`.
- `__repr__(self)` defines the developer/debugging representation returned by `repr(obj)`.

Both `Baratheon` and `Lannister` implement `__str__` returning:

```text
Vector: ('<family_name>', '<eyes>', '<hairs>')
```

and delegate `__repr__` directly to `self.__str__()`.

### Alternative Constructors with `@classmethod`

A `@classmethod` receives the class itself (`cls`) as its first parameter instead of an instance (`self`). This lets `Lannister.create_lannister(...)` act as a named factory constructor:

```python
@classmethod
def create_lannister(cls, first_name: str, is_alive: bool = True) -> "Lannister":
    return cls(first_name, is_alive)
```

Using `cls(...)` rather than hardcoding `Lannister(...)` ensures subclasses calling `create_lannister` receive instances of their own subclass.

## Functions & Class Breakdown

### `S1E7.py`

#### `Baratheon(Character)`

- Sets `family_name = "Baratheon"`, `eyes = "brown"`, `hairs = "dark"`.
- Implements `die()`, `__str__()`, and `__repr__()`.

#### `Lannister(Character)`

- Sets `family_name = "Lannister"`, `eyes = "blue"`, `hairs = "light"`.
- Implements `die()`, `__str__()`, `__repr__()`, and `@classmethod create_lannister(cls, first_name, is_alive=True)`.

### `tester.py`

Verifies inheritance from `Character`, family traits, `str()` and `repr()` output, `die()`, `create_lannister` defaults and return type, abstractness of `Character`, and docstrings.

---

# Exercise 02 — `DiamondTrap`: Multiple Inheritance, MRO & Properties

**Files:** `S1E9.py` · `S1E7.py` · `DiamondTrap.py` · `tester.py`

## Concepts Explained

### The Diamond Problem & C3 Linearization (MRO)

`King` inherits from both `Baratheon` and `Lannister`, which both inherit from `Character`:

```text
        Character (ABC)
         /          \
   Baratheon      Lannister
         \          /
             King
```

Python resolves attribute and `super()` lookups deterministically using **C3 Linearization**, stored in `King.__mro__`:

```text
(King, Baratheon, Lannister, Character, ABC, object)
```

Because `Baratheon` precedes `Lannister` in the base list `class King(Baratheon, Lannister)`, `super().__init__(first_name, is_alive)` invokes `Baratheon.__init__`, giving a newly created `King` Baratheon defaults (`family_name="Baratheon"`, `eyes="brown"`, `hairs="dark"`).

### Properties & Direct `self.__dict__` Storage

`King` exposes `eyes` and `hairs` as both explicit methods (`get_eyes`, `set_eyes`, `get_hairs`, `set_hairs`) and Python `property` descriptors:

```python
eyes = property(get_eyes, set_eyes, doc="Eyes color of the King.")
hairs = property(get_hairs, set_hairs, doc="Hairs color of the King.")
```

> [!NOTE]
> **Why `self.__dict__["eyes"]` instead of `self.eyes`?**
>
> Because `eyes` is a data descriptor on the class `King`, writing `self.eyes = color` inside `set_eyes()` would invoke `set_eyes()` again, causing infinite `RecursionError`. Reading and writing `self.__dict__["eyes"]` directly bypasses the descriptor while keeping `Joffrey.__dict__` identical in structure (`{'first_name': ..., 'eyes': ..., 'hairs': ...}`).

## Functions & Class Breakdown

### `DiamondTrap.py`

#### `King(Baratheon, Lannister)`

- `__init__(self, first_name: str, is_alive: bool = True)` — calls `super().__init__(first_name, is_alive)`.
- `get_eyes()` / `set_eyes(color)` — reads/updates `self.__dict__["eyes"]`.
- `get_hairs()` / `set_hairs(color)` — reads/updates `self.__dict__["hairs"]`.
- `eyes` / `hairs` — `property(...)` descriptors wrapping the getter/setter pairs.

### `tester.py`

Checks `isinstance` across `Baratheon`, `Lannister`, and `Character`, exact `King.__mro__`, default Baratheon traits, getter/setter synchronization with `__dict__`, property syntax (`Tommen.eyes = "grey"`), instance isolation, inherited `die()` and `str()`, and docstrings.

---

# Exercise 03 — `ft_calculator` (Scalar): Operator Overloading

**Files:** `ft_calculator.py` · `tester.py`

## Concepts Explained

### Arithmetic Dunder Methods

Python translates binary arithmetic operators on custom objects into special ("dunder") method calls:

| Expression | Dunder Method Invoked | Behavior in `calculator` |
|:---|:---|:---|
| `calc + s` | `calc.__add__(s)` | Adds `s` to every element in place and prints `self.vector` |
| `calc * s` | `calc.__mul__(s)` | Multiplies every element by `s` in place and prints `self.vector` |
| `calc - s` | `calc.__sub__(s)` | Subtracts `s` from every element in place and prints `self.vector` |
| `calc / s` | `calc.__truediv__(s)` | Divides every element by `s` in place (catching division by `0`) and prints `self.vector` |

### State Accumulation & Zero-Division Protection

Because each method mutates `self.vector` in place, sequential calls accumulate on the same instance (e.g., `v3 - 5` followed by `v3 / 5`). In `__truediv__`, checking `if object == 0` before dividing raises and catches `ZeroDivisionError`, leaving `self.vector` unchanged and printing the error message.

## Functions & Class Breakdown

### `ft_calculator.py`

#### `calculator`

- `__init__(self, vector: list[float]) -> None` — stores a copy converted to floats: `[float(x) for x in vector]`.
- `__add__`, `__mul__`, `__sub__`, `__truediv__` — apply scalar operations element-wise in place and print `self.vector`.

### `tester.py`

Captures stdout with `io.StringIO` and `contextlib.redirect_stdout` to test all four operations, negative/zero/float scalars, empty vectors, integer-to-float conversion, zero-division handling, chained accumulation, and docstrings.

---

# Exercise 04 — `ft_calculator` (Vector): `@staticmethod` & Vector Algebra

**Files:** `ft_calculator.py` · `tester.py`

## Concepts Explained

### Static Methods (`@staticmethod`)

A `@staticmethod` lives in a class's namespace for logical organization but receives neither `self` nor `cls`. It can therefore be called directly on the class without creating an instance:

```python
calculator.dotproduct(a, b)
```

(It can still be invoked through an instance such as `calculator().dotproduct(a, b)`.)

### Vector Operations Formulas

Given two equal-length vectors $\vec{u} = (u_0, \ldots, u_{n-1})$ and $\vec{v} = (v_0, \ldots, v_{n-1})$:

- **Dot product:**

  $$
  \vec{u} \cdot \vec{v} = \sum_{i=0}^{n-1} u_i \cdot v_i
  $$

- **Element-wise addition:**

  $$
  \vec{u} + \vec{v} = \left[\text{float}(u_0 + v_0), \ldots, \text{float}(u_{n-1} + v_{n-1})\right]
  $$

- **Element-wise subtraction:**

  $$
  \vec{u} - \vec{v} = \left[\text{float}(u_0 - v_0), \ldots, \text{float}(u_{n-1} - v_{n-1})\right]
  $$

All three methods leave the input lists `V1` and `V2` unmodified.

## Functions & Class Breakdown

### `ft_calculator.py`

#### `calculator`

- `dotproduct(V1: list[float], V2: list[float]) -> None` (`@staticmethod`) — prints `Dot product is: <result>`.
- `add_vec(V1: list[float], V2: list[float]) -> None` (`@staticmethod`) — prints `Add Vector is : <result>`.
- `sous_vec(V1: list[float], V2: list[float]) -> None` (`@staticmethod`) — prints `Sous Vector is: <result>`.

### `tester.py`

Uses `io.StringIO` + `redirect_stdout` to verify integer, float, orthogonal, zero, and negative vectors, input immutability, calling via an instance, and docstrings.

---

# Reference: Built-ins, Decorators & Dunder Methods

| Symbol | Category | Purpose in OOP |
|:---|:---|:---|
| `abc.ABC`, `@abstractmethod` | `abc` module | Define abstract base classes that cannot be instantiated directly (`ex00`–`ex02`) |
| `super()` | Built-in | Delegate method calls along the class MRO (`ex00`–`ex02`) |
| `@classmethod` | Built-in decorator | Define alternative factory constructors bound to `cls` (`ex01`) |
| `@staticmethod` | Built-in decorator | Define stateless utility methods callable without instantiation (`ex04`) |
| `property()` | Built-in descriptor | Bind getter/setter methods to attribute access syntax (`ex02`) |
| `__mro__`, `__dict__`, `__doc__` | Special attributes | Inspect C3 inheritance order, instance attribute storage, and docstrings (`ex00`–`ex04`) |
| `__init__`, `__str__`, `__repr__` | Dunder methods | Control object initialization and string representations (`ex00`–`ex03`) |
| `__add__`, `__mul__`, `__sub__`, `__truediv__` | Dunder methods | Overload `+`, `*`, `-`, and `/` operators (`ex03`) |
| `isinstance()`, `type()`, `all()`, `bool()` | Built-ins | Runtime inheritance verification and test assertions (`ex00`–`ex04`) |
| `io.StringIO`, `redirect_stdout` | `io` / `contextlib` | Capture printed output for automated test assertions (`ex03`, `ex04`) |
