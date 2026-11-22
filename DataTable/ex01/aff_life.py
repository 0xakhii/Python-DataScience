"""Display life expectancy for a selected country over time."""

import os
import matplotlib.pyplot as plt
from load_csv import load


def aff_life() -> None:
    """Load and display life expectancy for Morocco."""
    path = "/home/ojamal/Downloads/life_expectancy_years.csv"
    if not os.path.isfile(path):
        print("Error: life_expectancy_years.csv was not found")
        return

    dataset = load(path)
    if dataset is None:
        return

    country = "Morocco"
    if country not in dataset["country"].values:
        print(f"Error: country {country} was not found")
        return

    row = dataset.loc[dataset["country"] == country].iloc[0]
    year_columns = [column for column in dataset.columns
                    if column.isdigit()]
    if not year_columns:
        print("Error: no yearly columns were found")
        return
    years = [int(year) for year in year_columns]
    values = row[year_columns]

    plt.figure()
    plt.plot(years, values, label=country)
    plt.title(f"Life expectancy in {country}")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy (years)")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()


def main() -> None:
    """Run the life expectancy display function."""
    aff_life()


if __name__ == "__main__":
    main()
