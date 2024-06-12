# Write a program to sort a pandas DataFrame by a specific column.

import pandas as pd
df = pd.read_csv('Sales Data.csv')

df = df.sort_values('Quantity Ordered')               #ascending order and for decending order : df = df.sort_values('Quantity Ordered' , ascending=False)
print(df)