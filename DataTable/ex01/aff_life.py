"""Display life expectancy for a selected country over time."""

import os
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


def main() -> None:
    """Load and display life expectancy for Morocco."""
    path = find_dataset("/home/akhi/Downloads/life_expectancy_years.csv")
    if path is None:
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


if __name__ == "__main__":
    main()
