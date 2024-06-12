# Write a function to reset the index of a pandas DataFrame. 

import pandas as pd
df = pd.read_csv('Sales Data.csv')

df = df.reindex()
print(df)
 