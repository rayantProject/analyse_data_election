import os
import pandas as pd
from src.controllers.geographic import add_commune_geo


def main():
    dataset = pd.read_csv("dist/merged.csv")
    add_commune_geo(dataset)


if __name__ == "__main__":
    main()
