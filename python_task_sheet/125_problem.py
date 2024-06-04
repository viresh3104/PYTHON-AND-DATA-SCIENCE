# Given a 1D NumPy array, create a new array that contains only the unique elements from the original array, 
# sorted in descending order
import numpy as np
arr = np.random.random_integers(1,50,10)
print(arr)
arr = np.unique(arr)
new_arr = np.sort(arr)[::-1]
print(new_arr)