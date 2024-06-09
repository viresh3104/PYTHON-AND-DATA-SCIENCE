# Create a 1D array of 20 random integers between 1 and 50. Replace the maximum value with -1

import numpy as np


arr = np.random.random_integers(1,50,20)
print(arr)

max = np.argmax(arr)
arr[max] = -1
print(arr)




