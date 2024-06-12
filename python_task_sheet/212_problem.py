# Create a function to display the first 5 rows of a pandas DataFrame. 
import pandas as pd
def first_five_rows(df):
    df = df.head()
    return df

df = pd.read_csv("Sales Data.csv")
print(first_five_rows(df))