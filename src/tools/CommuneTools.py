import pandas as pd


def merge_by_commune(df1, df2):
    return pd.merge(df1, df2, on="commune")