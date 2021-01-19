import pandas as pd

def export(df):
    df.to_csv(r'~/Downloads/DataFrames/dataframe.csv', index = True)
