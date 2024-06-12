# Write a function to transpose a pandas DataFrame. 

import pandas as pd
data = {
'Company': ['GOOG', 'GOOG', 'MSFT','MSFT','FB','FB'],
'Person' : ['Sam','Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
'Sales'  : [200,120,340,124,243,350]
}

df = pd.DataFrame(data)
print(df)

df = df.transpose()
print(df)