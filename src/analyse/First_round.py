import pandas as pd

class FirstRound:
    file = "src/res/election/firstround.xlsx"

    def __init__(self):
        self.df = pd.read_excel(self.file)
        
    