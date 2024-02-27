import pandas as pd
import os


class Unemployment_analyse:
    file = "src/res/economic/unemployment.xlsx"

    removeRows = [0, 1, 2, 3]

    headers = ["code_insee", "commune", "annee", "nb_chomeurs"]

    removeColumns = ["annee"]

    def __init__(self):
        self.df = pd.read_excel(self.file, skiprows=self.removeRows, names=self.headers)
        self.df = self.df[self.df["annee"] == 2020]
        self.df = self.df.drop(columns=self.removeColumns)

    def get_data(self):
        return self.df

    def create_csv(self):
        if not os.path.exists("src/res/generate"):
            os.makedirs("src/res/generate")
            self.df.to_csv("src/res/generate/unemployment_worked.csv", index=False)
        else:
            if not os.path.exists("src/res/generate/unemployment_worked.csv"):
                self.df.to_csv("src/res/generate/unemployment_worked.csv", index=False)
            else:
                self.df.to_csv("src/res/generate/unemployment_worked.csv", index=False)

    def filter_post_code_by_start(self, start="69"):
        return self.df[self.df["code_insee"].astype(str).str.startswith(start)]
