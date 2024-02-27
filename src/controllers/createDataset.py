from src.analyse.Global import Global_anaylse as Gl
from src.analyse.Criminalities import Criminalities_analyse as Cr
from src.analyse.First_round import First_round_analyse as Fr
from src.analyse.Unemployment import Unemployment_analyse as Up
from src.tools.CommuneTools import merge_by_commune as MbC
from src.tools.CommuneTools import merge_by_code_insee as MbI

import os


def create():
    print("Chargement des données en cours...")
    Unemployment = Up()
    First_round = Fr()
    Criminalities = Cr()
    Glbl = Gl()  # Renommé Global
    print("Traitement des données en cours...")

    print("fusion des données en cours 25%...")
    merged1 = MbC(
        Unemployment.filter_post_code_by_start(), First_round.qui_a_gagne_id()
    )

    print("fusion des données en cours 50%...")
    merged2 = MbI(
        Criminalities.filter_post_code_by_start(),
        Glbl.filter_post_code_by_start(),
    )

    print("fusion des données en cours 75%...")
    merged3 = MbI(merged1, merged2)

    print("fusion des données en cours 100%...")
    if not os.path.exists("dist"):
        os.makedirs("dist")
        merged3.to_csv("dist/merged.csv", index=False)
    else:
        if not os.path.exists("dist/merged.csv"):
            merged3.to_csv("dist/merged.csv", index=False)
        else:
            merged3.to_csv("dist/merged.csv", index=False)
    print(
        "Traitement des données terminé. votre fichier est dans le dossier dist dist/merged.csv"
    )
