# Write a program to group a pandas DataFrame by a specific column and calculate the mean value for each group. 

import pandas as pd

df = pd.read_csv('Sales Data.csv')
print(df)

group_by = df.groupby('City').mean(numeric_only=True)
print(group_by)
