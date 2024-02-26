from src.analyse.Unemployment import Unemployment_analyse as Up
from src.analyse.First_round import First_round_analyse as Fr
from src.tools.CommuneTools import merge_by_commune as MbC

Unemployment = Up()
First_round = Fr()


def main():
    Unemployment.create_csv()


if __name__ == "__main__":
    main()
