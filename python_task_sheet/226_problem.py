# Create a program to drop duplicate rows from a pandas DataFrame. 

import pandas as pd
df = pd.read_csv('Sales Data.csv')
df = df.drop_duplicates()
print(df)