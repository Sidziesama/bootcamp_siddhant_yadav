import pandas as pd


def grouping(df):
    group = df.groupby('category')['value'].sum()
    return group