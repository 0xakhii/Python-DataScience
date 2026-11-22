"""Load and validate CSV datasets."""

import os
import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file and print its dimensions.

    Args:
        path (str): Path to the CSV file.

    Returns:
        pd.DataFrame | None: Loaded dataset or None when loading fails.
    """
    try:
        if not isinstance(path, str):
            raise AssertionError("Path must be a string")
        if not os.path.isfile(path):
            raise FileNotFoundError("File not found")
        if not path.lower().endswith(".csv"):
            raise ValueError("Invalid file format: expected .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except (AssertionError,
            FileNotFoundError,
            ValueError,
            pd.errors.ParserError) as error:
        print(f"Error: {error}")
        return None


def main() -> None:
    """Run a basic loader demonstration."""
    print(load("/home/ojamal/Downloads/life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
