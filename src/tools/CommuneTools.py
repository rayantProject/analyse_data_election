import pandas as pd


def merge_by_commune(df1, df2):
    return pd.merge(df1, df2, on="commune", how="inner")


def merge_by_code_insee(df1, df2):
    return pd.merge(df1, df2, on="code_insee", how="inner")
