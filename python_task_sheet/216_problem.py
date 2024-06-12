# Write a function to add a new column to a pandas DataFrame. 
import pandas as pd
df = pd.read_csv('Sales Data.csv')

def adding_new_coloum(df):
    df['new' ] = df['Quantity Ordered'] * df['Price Each']
    return df 

# print(adding_new_coloum(df))



# now remove this added coloum
# Implement a program to remove a column from a pandas DataFrame. 

# df = df.drop('new' , axis = 1)



