# Write a function that takes a NumPy array and replaces all negative values with 0.

import numpy as np 

arr = np.random.random_integers(-10,10,8)
print("orignal array :: ",arr)
arr[arr< 0] = 0
print("when changed all negative values to zero :: ",arr)