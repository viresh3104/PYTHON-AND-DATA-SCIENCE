# Implement a program to create a pandas DataFrame from a dictionary. 

import pandas as pd

given_dict = {1:['a','b','c'] ,2:['e','f','g'],3:['h','i','j']}
x = pd.DataFrame(given_dict)
print(x)