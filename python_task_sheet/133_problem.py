# Implement a program that generates a random 2D NumPy array and then calculates the row-wise mean and column-wise mean.
import numpy as np
arr = np.random.random_integers(10 ,size=(3,3))
print(arr)
row_mean = np.mean(arr, axis=1)
col_mean = np.mean(arr, axis=0)
print("row mean ::", row_mean)
print("coloum mean::",col_mean)
