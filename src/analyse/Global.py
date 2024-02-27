import pandas as pd
import os
import gdown

url = "https://drive.google.com/uc?id=1QTBLre4EveBvNSDCaq_W4fQtqUjHbuEX"


class Global_anaylse:
    # file = "src/res/global/global.csv"
    file = "src/res/down/global.csv"

    neededColumns = ["SNH20", "TP619", "CODGEO", "P19_POP"]
    renameColumns = {
        "SNH20": "salaire_net_horaire_moyen",
        "TP619": "taux_pauvrete",
        "CODGEO": "code_insee",
        "P19_POP": "population",
    }

    def __init__(self):

        if not os.path.exists(self.file):
            if not os.path.exists("src/res/down"):
                os.makedirs("src/res/down")
                gdown.download(url, self.file, quiet=False)
            else:
                gdown.download(url, self.file, quiet=False)
        self.df = pd.read_csv(self.file)
        self.df = self.df[self.df["COD_MOD"].str.startswith("69", na=False)]
        self.df = self.df[self.neededColumns]

    def get_data(self):
        return self.df

    def create_csv(self):
        if not os.path.exists("src/res/generate"):
            os.makedirs("src/res/generate")
            self.df.to_csv("src/res/generate/global.csv", index=False)
        else:
            if not os.path.exists("src/res/generate/global.csv"):
                self.df.to_csv("src/res/generate/global.csv", index=False)
            else:
                print("File already exists")
