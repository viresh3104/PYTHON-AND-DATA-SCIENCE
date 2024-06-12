# Implement a function to drop rows with missing values from a pandas DataFrame. 

import pandas as pd


df = pd.read_csv('Sales Data.csv')
print(df)
df = df.dropna()
print(df)