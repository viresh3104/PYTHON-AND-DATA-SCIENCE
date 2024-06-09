# Given a 2D array, find the column-wise mean of the array.

import numpy as np

arr = np.random.random_integers(1,20,size=(3,3))
print(arr)

mean = np.mean(arr, axis=0)
print(mean)