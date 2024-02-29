import pandas as pd
import os


geo_file = "src/res/geo/communes.csv"


def add_commune_geo(dataset):

    print("recuperation des données géographiques...")
    geo = pd.read_csv(geo_file)
    geo = geo[["code_commune_INSEE", "latitude", "longitude"]]
    geo = geo.drop_duplicates()
    dataset["code_insee"] = dataset["code_insee"].astype(str)
    merged_dataset = pd.merge(
        dataset, geo, left_on="code_insee", right_on="code_commune_INSEE", how="left"
    )
    merged_dataset.drop(columns=["code_commune_INSEE"], inplace=True)
    merged_dataset = merged_dataset.drop_duplicates()
    print("ajout des données géographiques")
    print("sauvegarde du fichier")
    merged_dataset.to_csv("dist/merged_geo.csv", index=False)
