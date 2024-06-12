# Write a program to perform element-wise subtraction on two pandas Series. 

import pandas as pd

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

list1 = pd.Series(list1)
print(list1)
list2 = pd.Series(list2)
print(list2)

list_3 = list1 - list2
print(list_3)