# Write a program to select a single column from a pandas DataFrame. 

import pandas as pd 
df = pd.read_csv("Sales Data.csv")

x = df['Product']                           
print(x)