# Given a 2D array, find the row with the maximum sum of elements.

import numpy as np

arr = np.random.random_integers(1,10,size=(3,3))
print(arr)


sum_of_row = np.sum(arr , axis=1)
print(np.max(sum_of_row))