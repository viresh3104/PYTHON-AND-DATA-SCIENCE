# Implement a program to calculate the mean of each row in a pandas Data Frame. 

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 6], 'C': [7, 8, 9]})
print(df)
  

df['Mean'] = df.mean(axis=1)
print(df)