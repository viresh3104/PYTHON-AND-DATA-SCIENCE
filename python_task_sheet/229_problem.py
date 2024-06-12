# Write a program to convert a pandas DataFrame to a NumPy array. 
import pandas as pd
data = {
'Company': ['GOOG', 'GOOG', 'MSFT','MSFT','FB','FB'],
'Person' : ['Sam','Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
'Sales'  : [200,120,340,124,243,350]
}

df = pd.DataFrame(data)
print(df)
df_to_arr = df.to_numpy()
print(df_to_arr)