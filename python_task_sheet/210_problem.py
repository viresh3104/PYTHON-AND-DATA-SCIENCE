# Write a program to create a pandas Series from a Python list. 
import pandas as pd

given_list = [1,2,3,4,5,6,7,8,9]
x = pd.Series(given_list)
print(x)