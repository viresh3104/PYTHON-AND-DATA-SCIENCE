# Implement a function to select multiple columns from a pandas DataFrame. 


import pandas as pd 
df = pd.read_csv("Sales Data.csv")

x = df[['Product','Sales']]                     
print(x)