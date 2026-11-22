"""Compare GDP and life expectancy projections for 1900."""

import os
import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


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


def projection_life() -> None:
    """Plot life expectancy against GDP per person for the year 1900."""
    base_dir = "/home/ojamal/Downloads"
    income_name = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    life_name = "life_expectancy_years.csv"
    income_path = f"{base_dir}/{income_name}"
    life_path = f"{base_dir}/{life_name}"

    if not os.path.isfile(income_path):
        print(f"Error: {income_name} was not found")
        return
    if not os.path.isfile(life_path):
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


def main() -> None:
    """Run the life expectancy and GDP projection function."""
    projection_life()


if __name__ == "__main__":
    main()
