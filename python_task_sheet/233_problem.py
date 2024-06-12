# Create a function to round the values in a pandas DataFrame to a specified number of decimal places. 

import pandas as pd
import math

df = pd.DataFrame({'a': [1.23456789, 2.34567890, 3.45678901]})

df['a'] = df['a'].apply(math.ceil)
print(df)