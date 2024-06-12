# Create a program to calculate the cumulative sum of values in a pandas Series. 

import pandas as pd

df = pd.DataFrame({'A': [2, 3, 8, 14]})

df['cumu_sum'] = df['A'].cumsum()
print(df)