# Implement a function to pivot a pandas DataFrame based on specified columns and aggregate values using a specific function

import pandas as pd
df = pd.read_csv('Sales Data.csv')


def pivot_dataframe(df, index, columns, values, aggfunc='mean'):
    pivoted_df = df.pivot_table(index=index, columns=columns, values=values, aggfunc=aggfunc)
    return pivoted_df

df = pd.read_csv('Sales Data.csv')
pivoted_df = pivot_dataframe(df, index='Product', columns='City', values='Sales', aggfunc='sum')
print(pivoted_df)