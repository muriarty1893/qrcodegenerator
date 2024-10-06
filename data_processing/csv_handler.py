import pandas as pd

def read_csv(filename='data.csv'):
    df = pd.read_csv(filename)
    return df.to_string(index=False)
