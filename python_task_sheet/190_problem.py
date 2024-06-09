# Generate a 1D array of 20 random integers between 1 and 100. Find the indices of the elements that are even.

import numpy as np

arr = np.random.randint(1,100+1,20)
print(arr)
even_arr = np.argwhere(arr % 2 == 0)
print(even_arr)

