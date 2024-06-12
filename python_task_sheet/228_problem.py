# Create a function to apply a custom function to each element of a pandas Series. 
import pandas as pd
df = pd.read_csv('Sales Data.csv')

def custom_func(x):
    return x*2

df = df['Quantity Ordered'].apply(custom_func)
print(df)

