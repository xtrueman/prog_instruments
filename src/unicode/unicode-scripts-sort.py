import pandas as pd

df = pd.read_csv("scripts.csv", sep='\t')

df.sort_values('Characters', ascending=False).head(15)
