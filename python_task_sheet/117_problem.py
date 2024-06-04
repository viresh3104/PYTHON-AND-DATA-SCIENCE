# Given a list of lists, create a 2D NumPy array and find the sum of elements in each row and column. 
import numpy as np
def sum(data):
    num_arr = np.array(data)
    sum_row = np.sum(num_arr , axis=1)
    sum_colo = np.sum(num_arr , axis=0)
    return sum_row , sum_colo



data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_rows, sum_columns = sum(data)
print("Sum of rows:", sum_rows)
print("Sum of columns:", sum_columns)