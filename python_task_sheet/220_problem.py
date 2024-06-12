# Create a program to calculate summary statistics (mean, median, min, max, etc.) for each column in a pandas DataFrame. 

import pandas as pd
df = pd.read_csv('Sales Data.csv')

df = df.describe()
print(df)