# Create a function to merge two pandas DataFrames based on a common column. 
import pandas as pd



left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'A': ['A', 'A1', 'A2', 'A3'],
'B': ['BO', 'B1', 'B2', 'B3']})


right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
'C': ['co', 'C1', 'C2', 'C3'],
'D': ['DO', 'D1', 'D2', 'D3']})


x = pd.merge(left,right  , on='key')
print(x)