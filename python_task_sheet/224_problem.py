# Write a program to fill missing values in a pandas DataFrame with a specified value. 

import pandas as pd
import numpy as np

dict = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(dict)
print(df)


df = df[['A','B','C']].fillna(value= df[['A','B','C']].mean())
print(df)