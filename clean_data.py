import pandas as pd

def clean_data(df):
    if df.empty:
        return df

    df.columns = df.columns.get_level_values(0)
    df.columns.name = None

    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.dropna()

    return df