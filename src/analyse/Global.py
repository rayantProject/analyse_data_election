import pandas as pd
import os
import gdown

url = "https://drive.google.com/uc?id=1QTBLre4EveBvNSDCaq_W4fQtqUjHbuEX"


class Global_anaylse:
    # file = "src/res/global/global.csv"
    file = "src/res/down/global.csv"
    dtype_mapping = {
        "CODGEO": str,  # Colonne à l'indice 0
    }
    neededColumns = [
        "SNHM21",
        "TP6021",
        "CODGEO",
        "P20_POP",
        "MED21",
        "P20_POPH",
        "P20_POPF",
        "P20_POP1529",
        "P20_POP3044",
        "P20_POP4559",
        "P20_POP6074",
        "P20_POP7589",
        "P20_SCOL1824",
        "P20_SCOL2529",
        "P20_SCOL30P",
    ]
    renameColumns = {
        "SNHM21": "salaire_net_horaire_moyen",
        "TP6021": "taux_pauvrete",
        "CODGEO": "code_insee",
        "P20_POP": "population",
        "MED21": "mediane_niveau_vie",
        "P20_POPH": "population_homme",
        "P20_POPF": "population_femme",
        "P20_POP1529": "population_15_29",
        "P20_POP3044": "population_30_44",
        "P20_POP4559": "population_45_59",
        "P20_POP6074": "population_60_74",
        "P20_POP7589": "population_75_89",
        "P20_SCOL1824": "population_scolarise_18_24",
        "P20_SCOL2529": "population_scolarise_25_29",
        "P20_SCOL30P": "population_scolarise_30_plus",
    }

    #  on va calculer le ratio de la population homme/femme
    def __init__(self):

        if not os.path.exists(self.file):
            if not os.path.exists("src/res/down"):
                os.makedirs("src/res/down")
                gdown.download(url, self.file, quiet=False)
            else:
                gdown.download(url, self.file, quiet=False)
        self.df = pd.read_csv(self.file, sep=";", dtype=self.dtype_mapping)
        self.df = self.df[self.neededColumns]
        self.df = self.df.rename(columns=self.renameColumns)

    def get_data(self):
        return self.df

    def create_csv(self):
        if not os.path.exists("src/res/generate"):
            os.makedirs("src/res/generate")
            self.df.to_csv("src/res/generate/global_worked.csv", index=False)
        else:
            if not os.path.exists("src/res/generate/global_worked.csv"):
                self.df.to_csv("src/res/generate/global_worked.csv", index=False)
            else:
                self.df.to_csv("src/res/generate/global_worked.csv", index=False)

    def filter_post_code_by_start(self, start="69"):
        return self.df[self.df["code_insee"].astype(str).str.startswith(start)]
