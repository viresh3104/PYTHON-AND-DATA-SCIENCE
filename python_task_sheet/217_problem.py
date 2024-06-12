# Create a function to filter rows from a pandas DataFrame based on multiple conditions. 

import pandas as pd
df = pd.read_csv('Sales Data.csv')



df = df.dropna()
print(df) 