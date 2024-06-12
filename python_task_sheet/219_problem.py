# Implement a function to rename columns in a pandas DataFrame. 

import pandas as pd
df = pd.read_csv('Sales Data.csv')


df = df.rename(columns= {'Order ID' : 'ID'})
print(df)
