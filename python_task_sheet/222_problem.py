# Implement a program to concatenate two pandas DataFrames vertically (stacking). 

import pandas as pd


df1 = pd.DataFrame({
'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['BO', 'B1', 'B2', 'B3'],
'C': ['co', 'C1', 'C2', 'C3'],
'D': ['DO', 'D1', 'D2', 'D3']},
index=[0, 1, 2, 3])


df2 = pd.DataFrame({
'A': ['A4', 'A5', 'A6', 'A7'],
'B': ['B4', 'B5', 'B6', 'B7'],
'C': ['C4', 'C5', 'C6', 'C7'],
'D': ['D4', 'D5', 'D6', 'D7']},
index = [4, 5, 6, 7])


concat_two_dfs = pd.concat([df1,df2])
print(concat_two_dfs)