"""Compare population projections for Morocco and Algeria."""

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


def population_value(value: object) -> float:
    """Convert a Gapminder population value to a numeric population."""
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
    """Load and compare population data from 1800 to 2050."""
    path = find_dataset("/home/ojamal/Downloads/population_total.csv")
    if path is None:
        print("Error: population_total.csv was not found")
        return

    dataset = load(path)
    if dataset is None:
        return

    years = [int(year) for year in dataset.columns
             if year.isdigit() and 1800 <= int(year) <= 2050]

    plt.figure()
    for country in ("Morocco", "Algeria"):
        if country not in dataset["country"].values:
            print(f"Error: country {country} was not found")
            return
        row = dataset.loc[dataset["country"] == country].iloc[0]
        values = [population_value(row[str(year)]) for year in years]
        plt.plot(years, values, label=country)

    plt.title("Population of Morocco and Algeria")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(title="Country")
    plt.ticklabel_format(axis="y", style="plain")
    plt.grid(alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()
