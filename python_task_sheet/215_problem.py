# Create a program to select specific rows from a pandas DataFrame based on a condition.

import pandas as pd 
df = pd.read_csv("Sales Data.csv")


x = df[df['Sales'] > 1000.00]
print(x)