# Create a program to calculate the correlation matrix for a pandas DataFrame.

import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [1, 2, 6], 'C': [7, 8, 9]})
df = df.corr()
print(df)




# A correlation matrix is a statistical technique used to evaluate the relationship between two variables in a data set.