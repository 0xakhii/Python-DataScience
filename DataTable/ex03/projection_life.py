"""Compare GDP and life expectancy projections for 1900."""

import os
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def find_dataset(filename: str) -> str | None:
    """Find a dataset in the DataTable or Downloads directories."""
    candidates = [
        filename,
        os.path.join("..", filename),
        os.path.join("..", "..", filename),
        os.path.join(os.path.expanduser("~"), "Downloads", filename),
    ]
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
    return None


def numeric_value(value: object) -> float:
    """Convert a Gapminder value containing M, B or k suffixes."""
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    multiplier = 1.0
    if text.endswith(("M", "m")):
        text = text[:-1]
        multiplier = 1_000_000.0
    elif text.endswith(("B", "b")):
        text = text[:-1]
        multiplier = 1_000_000_000.0
    elif text.endswith(("K", "k")):
        text = text[:-1]
        multiplier = 1_000.0
    try:
        return float(text) * multiplier
    except ValueError:
        return float("nan")


def main() -> None:
    """Plot life expectancy against GDP per person for the year 1900."""
    income_name = "/home/akhi/Downloads/income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_name = "/home/akhi/Downloads/life_expectancy_years.csv"
    income_path = find_dataset(income_name)
    life_path = find_dataset(life_name)

    if income_path is None:
        print(f"Error: {income_name} was not found")
        return
    if life_path is None:
        print(f"Error: {life_name} was not found")
        return

    income = load(income_path)
    life = load(life_path)
    if income is None or life is None:
        return

    if "1900" not in income.columns or "1900" not in life.columns:
        print("Error: the year 1900 was not found in both datasets")
        return

    income_values = income.set_index("country")["1900"].apply(numeric_value)
    life_values = life.set_index("country")["1900"].apply(numeric_value)
    points = pd.concat([income_values, life_values], axis=1, join="inner")
    points.columns = ["GDP per person", "Life expectancy"]
    points = points.replace([float("inf")], float("nan")).dropna()

    plt.figure()
    plt.scatter(points["GDP per person"], points["Life expectancy"],
                alpha=0.7, label="Countries")
    plt.title("Life expectancy versus GDP per person in 1900")
    plt.xlabel("Gross domestic product per person")
    plt.ylabel("Life expectancy (years)")
    plt.xscale("log")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()
