import pandas as pd

df = pd.read_csv('titanic.csv')
df.shape
df.head(5)

df.to_parquet('titanic.parquet')
