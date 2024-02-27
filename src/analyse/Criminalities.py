import pandas as pd
import os
import gdown

url = "https://drive.google.com/uc?id=1H-afTMfO6KlW5aQeoYnxhz6DoHnynXVO"


def arrondir_nombre(nombre):
    nombre = nombre.replace(",", ".") if isinstance(nombre, str) else nombre
    nombre_float = float(nombre)
    decimale = nombre_float - int(nombre_float)
    premiere_decimale = int(decimale * 10)
    if premiere_decimale < 5:
        nombre_arrondi = int(nombre_float)
    else:
        nombre_arrondi = int(nombre_float) + 1

    return nombre_arrondi


class Criminalities_analyse:
    file = "src/res/down/criminalities.csv"
    removeColumns = [
        "classe",
        "unité.de.compte",
        "tauxpourmille",
        "millPOP",
        "LOG",
        "millLOG",
        "valeur.publiée",
        "faits",
        "complementinfoval",
        "complementinfotaux",
        "POP",
    ]

    rename = {
        "CODGEO_2023": "code_insee",
    }

    def __init__(self):
        if not os.path.exists(self.file):
            if not os.path.exists("src/res/down"):
                os.makedirs("src/res/down")
                gdown.download(url, self.file, quiet=False)
            else:
                gdown.download(url, self.file, quiet=False)
        self.df = pd.read_csv(self.file, sep=";")
        self.df = self.df[self.df["annee"] != "16"]
        self.df["nb_crimes"] = self.df.apply(
            lambda row: (
                arrondir_nombre(row["faits"])
                if row["valeur.publiée"] == "diff"
                else arrondir_nombre(row["complementinfoval"])
            ),
            axis=1,
        )
        self.df = self.df.rename(columns=self.rename)
        # self.df = (
        #     self.df.groupby(["code_insee"])
        #     .agg(nb_crimes_sum=("nb_crimes", "sum"))
        #     .reset_index()
        # )
        self.df = self.df.drop(columns=self.removeColumns)

    def create_csv(self):
        if not os.path.exists("src/res/generate"):
            os.makedirs("src/res/generate")
            self.df.to_csv("src/res/generate/criminalities_worked.csv", index=False)
        else:
            if not os.path.exists("src/res/generate/criminalities_worked.csv"):
                self.df.to_csv("src/res/generate/criminalities_worked.csv", index=False)
            else:
                print("File already exists")

    def get_data(self):
        return self.df
