import pandas as pd
import os


class First_round_analyse:
    file = "src/res/election/firstround.xlsx"
    ideologiesOfCandidatesFile = "src/res/election/canditats_ideologies.json"

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

    renameColumns = {
        "Libellé de la commune": "commune",
        "Libellé du département": "department",
        "Nom": "ARTHAUD",
        "prénom": "NATHALIE",
        "Voix": "voix Nathalie Arthaud",
        "Voix/Ins": "voix/ins Nathalie Arthaud",
        "Voix/Exp": "voix/exp Nathalie Arthaud",
        "Unnamed: 28": "ROUSSEL",
        "Unnamed: 29": "FABIEN",
        "Unnamed: 30": "Voix Fabien Roussel",
        "Unnamed: 31": "Voix/Ins Fabien Roussel",
        "Unnamed: 32": "Voix/Exp Fabien Roussel",
        "Unnamed: 35": "MACRON",
        "Unnamed: 36": "EMMANUEL",
        "Unnamed: 37": "Voix Emmanuel Macron",
        "Unnamed: 38": "Voix/Ins Emmanuel Macron",
        "Unnamed: 39": "Voix/Exp Emmanuel Macron",
        "Unnamed: 42": "LASSALLE",
        "Unnamed: 43": "JEAN",
        "Unnamed: 44": "Voix Jean Lassalle",
        "Unnamed: 45": "Voix/Ins Jean Lassalle",
        "Unnamed: 46": "Voix/Exp Jean Lassalle",
        "Unnamed: 49": "LE PEN",
        "Unnamed: 50": "MARINE",
        "Unnamed: 51": "Voix Marine Le Pen",
        "Unnamed: 52": "Voix/Ins Marine Le Pen",
        "Unnamed: 53": "Voix/Exp Marine Le Pen",
        "Unnamed: 56": "ZEMMOUR",
        "Unnamed: 57": "ERIC",
        "Unnamed: 58": "Voix Eric Zemmour",
        "Unnamed: 59": "Voix/Ins Eric Zemmour",
        "Unnamed: 60": "Voix/Exp Eric Zemmour",
        "Unnamed: 63": "MÉLENCHON",
        "Unnamed: 64": "JEAN-LUC",
        "Unnamed: 65": "Voix Jean-Luc Mélenchon",
        "Unnamed: 66": "Voix/Ins Jean-Luc Mélenchon",
        "Unnamed: 67": "Voix/Exp Jean-Luc Mélenchon",
        "Unnamed: 70": "HIDALGO",
        "Unnamed: 71": "ANNE",
        "Unnamed: 72": "Voix Anne Hidalgo",
        "Unnamed: 73": "Voix/Ins Anne Hidalgo",
        "Unnamed: 74": "Voix/Exp Anne Hidalgo",
        "Unnamed: 77": "JADOT",
        "Unnamed: 78": "YANNICK",
        "Unnamed: 79": "Voix Yannick Jadot",
        "Unnamed: 80": "Voix/Ins Yannick Jadot",
        "Unnamed: 81": "Voix/Exp Yannick Jadot",
        "Unnamed: 84": "PECRESSE",
        "Unnamed: 85": "VALERIE",
        "Unnamed: 86": "Voix Valérie Pécresse",
        "Unnamed: 87": "Voix/Ins Valérie Pécresse",
        "Unnamed: 88": "Voix/Exp Valérie Pécresse",
        "Unnamed: 91": "POUTOU",
        "Unnamed: 92": "PHILIPPE",
        "Unnamed: 93": "Voix Philippe Poutou",
        "Unnamed: 94": "Voix/Ins Philippe Poutou",
        "Unnamed: 95": "Voix/Exp Philippe Poutou",
        "Unnamed: 98": "DUPONT-AIGNAN",
        "Unnamed: 99": "NICOLAS",
        "Unnamed: 100": "Voix Nicolas Dupont-Aignan",
        "Unnamed: 101": "Voix/Ins Nicolas Dupont-Aignan",
        "Unnamed: 102": "Voix/Exp Nicolas Dupont-Aignan",
    }

    def __init__(self):
        self.df = pd.read_excel(self.file)
        self.df = self.df.drop(columns=self.removeColumns)
        self.df = self.df.rename(columns=self.renameColumns)
        ideologies = pd.read_json(self.ideologiesOfCandidatesFile)
        for index, row in ideologies.iterrows():
            self.df["ideologies " + row["candidat"]] = row["ideologies"]

    def get_data(self):
        return self.df

    def create_csv(self):
        if not os.path.exists("src/res/election/firstround_worked.csv"):
            self.df.to_csv("src/res/election/firstround.csv", index=False)
        else:
            print("File already exists")

    def filter_by_department(self, department="Rhône"):
        return self.df[self.df["department"] == department]

    def get_communes_only_by_department(self, department="Rhône"):
        return self.filter_by_department(department)["commune"]
