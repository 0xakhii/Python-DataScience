# Complete Guide to the Array Folder (`ex00` – `ex05`)

> This guide explains every exercise in **Module 1 — Array**, covering numerical validation, 2D array slicing, NumPy array shapes and broadcasting, OpenCV image loading and color-space conversion, manual matrix transposition, and RGB channel-level color filters.

## Table of Contents

- [Directory Structure Overview](#directory-structure-overview)
- [Exercise 00 — give_bmi](#exercise-00--give_bmi-bmi-calculation--thresholding)
- [Exercise 01 — array2D](#exercise-01--array2d-2d-array-slicing--shapes)
- [Exercise 02 — load_image](#exercise-02--load_image-loading-images--bgr-to-rgb-conversion)
- [Exercise 03 — zoom](#exercise-03--zoom-grayscale-conversion-cropping--axis-expansion)
- [Exercise 04 — rotate](#exercise-04--rotate-manual-matrix-transposition)
- [Exercise 05 — pimp_image](#exercise-05--pimp_image-rgb-channel-filters--restricted-operators)
- [Reference](#reference-built-ins-numpy-opencv--matplotlib-utilities)

## Directory Structure Overview

| Exercise | Files | Core concepts |
|:---|:---|:---|
| `ex00` | `give_bmi.py` | BMI formula, parallel list validation, boolean threshold masking |
| `ex01` | `array2D.py` | 2D lists, `np.array()`, `.shape` inspection, index bounds validation, row slicing |
| `ex02` | `load_image.py` | `cv2.imread()`, BGR-to-RGB slicing (`[:, :, ::-1]`), file path & format validation |
| `ex03` | `load_image.py`, `zoom.py` | `cv2.cvtColor()` grayscale conversion, 2D array cropping, `np.newaxis`, `plt.imshow()` |
| `ex04` | `load_image.py`, `rotate.py` | Manual matrix transpose ($A^T_{j, i} = A_{i, j}$), `np.zeros()`, shape & dtype preservation |
| `ex05` | `load_image.py`, `pimp_image.py` | Non-mutating `.copy()`, RGB channel isolation, inversion, grayscale via `mean()` & `np.repeat()` |

---

# Exercise 00 — `give_bmi`: BMI Calculation & Thresholding

**Files:** `give_bmi.py`

## Concepts Explained

### Body Mass Index (BMI) Formula

For each pair of height $h_i$ (in meters) and weight $w_i$ (in kilograms):

$$
\text{BMI}_i = \frac{w_i}{h_i^2}
$$

### Validation & Thresholding

- Both `height` and `weight` must have the same length; otherwise an `AssertionError` is raised and `[]` is returned.
- Each element is validated as numeric and non-negative (`weight[i] < 0 or height[i] < 0` raises `AssertionError`).
- `apply_limit` maps each BMI score to a boolean flag indicating whether it strictly exceeds `limit` ($\text{BMI}_i > \text{limit}$).

## Functions Breakdown

### `give_bmi.py`

#### `give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]`

- Checks `len(height) == len(weight)`.
- Validates numeric convertibility (`int()`, `float()`) and non-negativity.
- Computes `weight[i] / (height[i] * height[i])` for each index.
- Catches `ValueError` and `AssertionError`, printing the message and returning `[]` on error.

#### `apply_limit(bmi: list[int | float], limit: int) -> list[bool]`

Returns a list of booleans where index `i` is `True` if `bmi[i] > limit` and `False` otherwise.

---

# Exercise 01 — `array2D`: 2D Array Slicing & Shapes

**Files:** `array2D.py`

## Concepts Explained

### NumPy `.shape` for 2D Arrays

A rectangular 2D list with $R$ rows and $C$ columns converts via `np.array(family)` into a 2D `np.ndarray` with:

```python
npArr.shape  # (R, C)
```

For example, 4 rows of `[height, weight]` pairs have shape `(4, 2)`. Slicing 2 rows yields shape `(2, 2)`.

### Input & Bounds Validation

- Verifies `type(family) is list`; otherwise raises `ValueError`.
- Verifies `abs(start) < len(family)` and `abs(end) < len(family)`; otherwise raises `ValueError`.
- Catches `ValueError`, prints the message, and returns `[]`.

## Functions Breakdown

### `array2D.py`

#### `slice_me(family: list, start: int, end: int) -> list`

- Converts `family` to a NumPy array and prints `My shape is: <shape>`.
- Iterates from `abs(start)` up to `abs(end)`, appending rows to `newArr`.
- Converts `newArr` to a NumPy array, prints `My new shape is: <new_shape>`, and returns `newArr`.

---

# Exercise 02 — `load_image`: Loading Images & BGR-to-RGB Conversion

**Files:** `load_image.py`

## Concepts Explained

### Digital Images as 3D NumPy Arrays

A color image of height $H$ pixels and width $W$ pixels is represented as a 3D `uint8` tensor of shape:

$$
(H, W, C), \qquad C = 3 \text{ channels } \in [0, 255]
$$

### OpenCV's BGR Convention

`cv2.imread()` decodes images in **BGR** (Blue, Green, Red) channel order rather than **RGB**. Reversing the third axis with NumPy step slicing converts BGR to RGB in a single view operation:

```python
img_rgb = img[:, :, ::-1]
```

### Defensive File Checks

Before decoding, `ft_load` checks:

1. `isinstance(path, str)` (`AssertionError`)
2. `os.path.exists(path)` (`FileNotFoundError`)
3. Supported extension `.jpg`, `.jpeg`, or `.png` (`FileExistsError`)
4. `img is not None` after `cv.imread(path)` (`ValueError`)

## Functions Breakdown

### `load_image.py`

#### `ft_load(path: str) -> np.ndarray | None`

Loads an image from `path`, prints its `(height, width, channels)` shape and RGB pixel values, and returns the RGB `np.ndarray` (or `None` on failure).

#### `main()`

Demonstrates `ft_load` on `landscape.jpg`.

---

# Exercise 03 — `zoom`: Grayscale Conversion, Cropping & Axis Expansion

**Files:** `load_image.py` · `zoom.py`

## Concepts Explained

### Grayscale Conversion & Spatial Cropping

1. **RGB to Grayscale:** `cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)` collapses the 3 RGB channels into a single luminance plane, changing shape from $(H, W, 3)$ to $(H, W)$.
2. **2D Slicing (Zooming):** Selecting rows `100:500` and columns `450:850` extracts a $400 \times 400$ square sub-image:

   ```python
   cropped = gray[100:500, 450:850]
   ```

3. **Adding a Channel Dimension:** Indexing with `np.newaxis` reshapes `(400, 400)` into `(400, 400, 1)` to keep an explicit channel axis:

   ```python
   cropped = cropped[:, :, np.newaxis]
   ```

4. **Display:** `cropped.squeeze()` drops the length-1 axis back to `(400, 400)` for `plt.imshow(..., cmap="gray")`, with axis ticks every 50 pixels (`np.arange(0, 351, 50)`).

## Functions Breakdown

### `zoom.py`

#### `zoom(path: str = "animal.jpeg") -> np.ndarray | None`

- Loads `path` via `ft_load`.
- Asserts `img.shape[0] >= 500` and `img.shape[1] >= 850`.
- Converts to grayscale, crops `[100:500, 450:850]`, expands to `(400, 400, 1)`, prints the new shape and array, displays it with Matplotlib, and returns `cropped`.

#### `main()`

Calls `zoom` on `animal.jpeg`.

---

# Exercise 04 — `rotate`: Manual Matrix Transposition

**Files:** `load_image.py` · `rotate.py`

## Concepts Explained

### Matrix Transposition

Transposing a 2D image matrix $A$ of shape $(R, C)$ swaps its row and column indices to produce $A^T$ of shape $(C, R)$:

$$
(A^T)_{j, i} = A_{i, j} \qquad \text{for } 0 \le i < R,\; 0 \le j < C
$$

Instead of calling `np.transpose()` or `.T`, `rotate.py` computes the transpose explicitly with nested loops:

```python
transposed = np.zeros((cols, rows, 3), dtype=cropped.dtype)
for i in range(rows):
    for j in range(cols):
        transposed[j, i] = cropped[i, j]
```

> [!NOTE]
> **Broadcasting single-channel values into 3 channels:** Because `cropped[i, j]` has shape `(1,)` and `transposed[j, i]` has shape `(3,)`, NumPy automatically broadcasts the grayscale intensity across all three RGB channels, producing an output of shape `(400, 400, 3)` that renders identically in grayscale.

## Functions Breakdown

### `rotate.py`

#### `zoom(path: str) -> np.ndarray | None`

Loads `path` with `ft_load`, converts to grayscale, crops `[100:500, 450:850]`, and returns the `(400, 400, 1)` array.

#### `rotate(path: str) -> None`

- Obtains the cropped image from `zoom(path)` and prints its shape and pixel array.
- Allocates `transposed` with `np.zeros` and copies `cropped[i, j]` to `transposed[j, i]`.
- Prints the transposed shape and pixels, then displays the result with `plt.imshow(..., cmap="gray")`.

#### `main() -> None`

Runs `rotate` on `animal.jpeg`.

---

# Exercise 05 — `pimp_image`: RGB Channel Filters & Restricted Operators

**Files:** `load_image.py` · `pimp_image.py`

## Concepts Explained

### Immutability via `.copy()`

Because NumPy slices return views sharing the same underlying memory buffer, mutating a filter's input array in place would corrupt subsequent filters. `_prepare()` validates that the input is a 3-channel 3D `np.ndarray` and returns `array.copy()`.

### Color Filter Transformations & Operator Constraints

Each filter demonstrates a different vectorized NumPy operation on an $(H, W, 3)$ `uint8` array whose channels are `[R=0, G=1, B=2]`:

| Function | Formula / Operation | Operators Used | Visual Effect |
|:---|:---|:---|:---|
| `ft_invert` | `255 - result` | `=`, `-` | Photographic color negative |
| `ft_red` | `G = G * 0`, `B = B * 0` | `=`, `*` | Retains only red channel |
| `ft_green` | `R = R - R`, `B = B - B` | `=`, `-` | Retains only green channel |
| `ft_blue` | `R = 0`, `G = 0` | `=` | Retains only blue channel |
| `ft_grey` | `mean(axis=2, keepdims=True) / 1`, repeated ×3 | `=`, `/` | Equal-weight RGB average grayscale |

For `ft_grey`, casting to `np.float32` before calling `.mean(axis=2, keepdims=True)` avoids integer overflow during summation, and `np.repeat(..., 3, axis=2)` restores a 3-channel `(H, W, 3)` `uint8` image.

## Functions Breakdown

### `pimp_image.py`

#### `_prepare(array: np.ndarray) -> np.ndarray | None`

Checks `isinstance(array, np.ndarray)`, `array.ndim == 3`, and `array.shape[2] == 3`; returns `array.copy()` or `None` if invalid.

#### `_show(array: np.ndarray, title: str) -> np.ndarray`

Prints the shape and pixel array, displays the image in a titled Matplotlib figure with axes hidden (`plt.axis("off")`), and returns `array`.

#### `ft_invert`, `ft_red`, `ft_green`, `ft_blue`, `ft_grey`

Each validates and clones the input via `_prepare`, applies its vectorized NumPy transformation, and delegates display/return to `_show`.

#### `main() -> None`

Loads `landscape.jpg`, displays the original image followed by all five filters, and prints `ft_invert.__doc__`.

---

# Reference: Built-ins, NumPy, OpenCV & Matplotlib Utilities

| Symbol | Category | Purpose in Array |
|:---|:---|:---|
| `np.array()`, `.shape`, `.ndim`, `.dtype` | NumPy | Convert lists to arrays and inspect array dimensions and data types (`ex01`–`ex05`) |
| `np.newaxis`, `.squeeze()` | NumPy | Add or remove singleton channel dimensions (`ex03`, `ex04`) |
| `np.zeros()`, `.copy()` | NumPy | Allocate output buffers and prevent in-place mutation (`ex04`, `ex05`) |
| `np.arange()` | NumPy | Generate evenly spaced tick positions for image axes (`ex03`, `ex04`) |
| `.astype()`, `.mean()`, `np.repeat()` | NumPy | Compute floating-point grayscale averages and rebuild 3-channel `uint8` arrays (`ex05`) |
| `img[:, :, ::-1]` | NumPy slicing | Reverse BGR channels to RGB without copying data (`ex02`–`ex05`) |
| `cv2.imread()` | OpenCV | Decode JPEG/PNG image files into BGR NumPy arrays (`ex02`–`ex05`) |
| `cv2.cvtColor(..., COLOR_RGB2GRAY)` | OpenCV | Convert 3-channel RGB images to single-channel grayscale (`ex03`, `ex04`) |
| `plt.figure()`, `plt.imshow()`, `plt.show()` | Matplotlib | Render RGB and grayscale arrays in GUI windows (`ex03`–`ex05`) |
| `plt.xticks()`, `plt.yticks()`, `plt.axis("off")` | Matplotlib | Configure pixel coordinate ticks or hide axes (`ex03`–`ex05`) |
| `os.path.exists()` | `os` module | Verify image file paths before reading (`ex02`–`ex05`) |
| `isinstance()`, `abs()`, `len()`, `range()` | Built-ins | Type checking, bounds checks, and loop indexing (`ex00`–`ex05`) |
