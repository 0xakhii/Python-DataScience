# Complete Guide to the DataTable Folder (`ex00` – `ex03`)

> This guide explains every exercise in **Module 2 — DataTable**, covering CSV ingestion and validation with Pandas, tabular row/column filtering, Gapminder unit-suffix parsing (`K`, `M`, `B`), multi-dataset inner joins, and data visualization with Matplotlib.

## Table of Contents

- [Directory Structure Overview](#directory-structure-overview)
- [Exercise 00 — load_csv](#exercise-00--load_csv-csv-loading--validation-with-pandas)
- [Exercise 01 — aff_life](#exercise-01--aff_life-single-country-time-series-plotting)
- [Exercise 02 — aff_pop](#exercise-02--aff_pop-unit-suffix-parsing--country-comparison)
- [Exercise 03 — projection_life](#exercise-03--projection_life-joining-datasets--log-scale-scatter-plots)
- [Reference](#reference-built-ins-pandas--matplotlib-utilities)

## Directory Structure Overview

| Exercise | Files | Core concepts |
|:---|:---|:---|
| `ex00` | `load_csv.py` | `pd.read_csv()`, `.shape` reporting, defensive path/extension/parser error handling |
| `ex01` | `load_csv.py`, `aff_life.py` | Boolean row filtering (`.loc`), numeric column selection, line plotting with Matplotlib |
| `ex02` | `load_csv.py`, `aff_pop.py` | Parsing `K`/`M`/`B` suffixes, year-range filtering (`1800`–`2050`), multi-series plots, plain y-axis formatting |
| `ex03` | `load_csv.py`, `projection_life.py` | `.set_index()`, `pd.concat(..., join="inner")`, `inf`/`NaN` cleaning, logarithmic scatter plot |

---

# Exercise 00 — `load_csv`: CSV Loading & Validation with Pandas

**Files:** `load_csv.py`

## Concepts Explained

### Tabular Data as a `pandas.DataFrame`

`pd.read_csv(path)` parses a comma-separated file into a 2D labeled `DataFrame`, exposing its row and column counts via `dataset.shape` as `(n_rows, n_columns)`.

### Defensive Validation Pipeline

Before calling `pd.read_csv`, `load()` verifies:

1. `isinstance(path, str)` — ensures the path is a string (`AssertionError`).
2. `os.path.isfile(path)` — verifies that a regular file exists at `path` (`FileNotFoundError`).
3. `path.lower().endswith(".csv")` — enforces the `.csv` extension (`ValueError`).
4. Catches `(AssertionError, FileNotFoundError, ValueError, pd.errors.ParserError)`, prints `Error: <message>`, and returns `None` instead of crashing.

## Functions Breakdown

### `load_csv.py`

#### `load(path: str) -> pd.DataFrame | None`

Validates `path`, loads the CSV into a `DataFrame`, prints `Loading dataset of dimensions <shape>`, and returns the `DataFrame` (or `None` on error).

#### `main() -> None`

Demonstrates `load()` on `life_expectancy_years.csv` (present in `ex00/load_csv.py`; omitted in the imported helper copies inside `ex01`–`ex03`).

---

# Exercise 01 — `aff_life`: Single-Country Time-Series Plotting

**Files:** `load_csv.py` · `aff_life.py`

## Concepts Explained

### Selecting a Row & Filtering Yearly Columns

Gapminder CSV files store one country per row and one calendar year per column:

```text
country  | 1800 | 1801 | ... | 2100
Morocco  | 29.0 | 29.0 | ... | 86.2
```

To extract a single country's time series:

1. Check membership in `dataset["country"].values`.
2. Select the matching row with `dataset.loc[dataset["country"] == country].iloc[0]`.
3. Filter year headers using `[column for column in dataset.columns if column.isdigit()]` and convert them to integers for the x-axis.

### Chart Configuration

`aff_life()` plots `years` vs. `values` with a descriptive title (`"Life expectancy in Morocco"`), axis labels (`"Year"`, `"Life expectancy (years)"`), legend, and subtle grid (`alpha=0.3`).

## Functions Breakdown

### `aff_life.py`

#### `aff_life() -> None`

Loads `life_expectancy_years.csv`, verifies `"Morocco"` and yearly columns exist, extracts the time series, and renders the Matplotlib line chart.

#### `main() -> None`

Entry point invoking `aff_life()`.

---

# Exercise 02 — `aff_pop`: Unit-Suffix Parsing & Country Comparison

**Files:** `load_csv.py` · `aff_pop.py`

## Concepts Explained

### Parsing Abbreviated Numeric Strings

Gapminder population tables encode large numbers using human-readable suffixes rather than raw integers:

| Suffix | Multiplier | Example | Parsed Value |
|:---|:---|---:|---:|
| `K` / `k` | $10^3$ (`1_000.0`) | `"520k"` | `520000.0` |
| `M` / `m` | $10^6$ (`1_000_000.0`) | `"37.5M"` | `37500000.0` |
| `B` / `b` | $10^9$ (`1_000_000_000.0`) | `"1.4B"` | `1400000000.0` |
| None | $1$ (`1.0`) | `"980"` | `980.0` |

Values that fail `float()` conversion gracefully degrade to `float("nan")`, which Matplotlib skips when drawing line segments.

### Range Filtering & Plain Axis Formatting

- Year columns are restricted to `1800 <= int(year) <= 2050`.
- Both `"Morocco"` and `"Algeria"` are plotted on the same `plt.figure()` with distinct legend labels.
- `plt.ticklabel_format(axis="y", style="plain")` disables default scientific notation (`1e7`) on the y-axis so population values remain directly readable.

## Functions Breakdown

### `aff_pop.py`

#### `population_value(value: object) -> float`

Converts a numeric value or suffixed string (`K`/`M`/`B`, case-insensitive) into a `float`, returning `float("nan")` if parsing fails.

#### `aff_pop() -> None`

Loads `population_total.csv`, filters years `1800`–`2050`, converts values for Morocco and Algeria, and renders a comparative multi-line plot.

#### `main() -> None`

Entry point invoking `aff_pop()`.

---

# Exercise 03 — `projection_life`: Joining Datasets & Log-Scale Scatter Plots

**Files:** `load_csv.py` · `projection_life.py`

## Concepts Explained

### Aligning Two Datasets with an Inner Join

GDP per capita and life expectancy live in two separate CSV files whose country lists may not match identically. Alignment is performed cleanly through Pandas index matching:

```python
income_values = income.set_index("country")["1900"].apply(numeric_value)
life_values = life.set_index("country")["1900"].apply(numeric_value)
points = pd.concat([income_values, life_values], axis=1, join="inner")
```

- `.set_index("country")` promotes country names to the Series index.
- `pd.concat(..., axis=1, join="inner")` places both metrics side by side and keeps only countries present in **both** datasets.
- `.replace([float("inf")], float("nan")).dropna()` drops missing or infinite entries before plotting.

### Logarithmic X-Axis for Income Distributions

Because GDP per person spans orders of magnitude across countries, plotting it on a logarithmic scale (`plt.xscale("log")`) spreads low-income and high-income countries evenly across the horizontal axis, revealing the classic Preston curve relationship between wealth and life expectancy in 1900.

## Functions Breakdown

### `projection_life.py`

#### `numeric_value(value: object) -> float`

Converts raw numbers or `K`/`M`/`B`-suffixed Gapminder strings into floats (or `NaN` on invalid strings).

#### `projection_life() -> None`

- Validates and loads `income_per_person_gdppercapita_ppp_inflation_adjusted.csv` and `life_expectancy_years.csv`.
- Verifies that column `"1900"` exists in both datasets.
- Aligns both series by country via inner join, removes `inf`/`NaN` rows, and draws a scatter plot (`alpha=0.7`) with `plt.xscale("log")`.

#### `main() -> None`

Entry point invoking `projection_life()`.

---

# Reference: Built-ins, Pandas & Matplotlib Utilities

| Symbol | Category | Purpose in DataTable |
|:---|:---|:---|
| `pd.read_csv()`, `pd.errors.ParserError` | Pandas | Parse CSV files into `DataFrame`s and catch malformed CSV errors (`ex00`–`ex03`) |
| `DataFrame.shape`, `.columns`, `.values` | Pandas | Inspect dataset dimensions, column labels, and underlying arrays (`ex00`–`ex03`) |
| `DataFrame.loc[]`, `.iloc[0]` | Pandas | Label-based row filtering and positional extraction (`ex01`, `ex02`) |
| `DataFrame.set_index()`, `Series.apply()` | Pandas | Index data by country and vector-apply custom suffix parsers (`ex03`) |
| `pd.concat(..., axis=1, join="inner")` | Pandas | Combine two country-indexed series into an aligned table (`ex03`) |
| `.replace()`, `.dropna()` | Pandas | Clean infinite and missing values prior to plotting (`ex03`) |
| `plt.plot()`, `plt.scatter()` | Matplotlib | Draw time-series line plots and cross-sectional scatter plots (`ex01`–`ex03`) |
| `plt.xscale("log")` | Matplotlib | Apply logarithmic scaling to the GDP x-axis (`ex03`) |
| `plt.ticklabel_format(style="plain")` | Matplotlib | Display full population numbers instead of scientific notation (`ex02`) |
| `plt.title()`, `xlabel()`, `ylabel()`, `legend()`, `grid()` | Matplotlib | Annotate figures for readable charts (`ex01`–`ex03`) |
| `os.path.isfile()` | `os` module | Verify CSV file existence before reading (`ex00`–`ex03`) |
| `str.isdigit()`, `str.strip()`, `str.endswith()` | String methods | Identify year columns and parse `K`/`M`/`B` unit suffixes (`ex00`–`ex03`) |
