
import pandas as pd


class Criminalities_analyse:
    file = "src/res/geo/criminalities.csv"
    removeColumns = [
        "Etat saisie",
        "Unnamed: 27",
        "Sexe",
        "Unnamed: 26",
        "Unnamed: 27",
        "Unnamed: 33",
        "Unnamed: 34",
        "Unnamed: 40",
        "Unnamed: 41",
        "Unnamed: 47",
        "Unnamed: 48",
        "Unnamed: 54",
        "Unnamed: 55",
        "Unnamed: 61",
        "Unnamed: 62",
        "Unnamed: 68",
        "Unnamed: 69",
        "Unnamed: 75",
        "Unnamed: 76",
        "Unnamed: 82",
        "Unnamed: 83",
        "Unnamed: 89",
        "Unnamed: 90",
        "Unnamed: 96",
        "Unnamed: 97",
    ]
    
    
    def __init__(self):
        self.df = pd.read_csv(self.file)