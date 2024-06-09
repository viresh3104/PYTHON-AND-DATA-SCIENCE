# Generate a random 4x4 matrix and replace all elements that are less than the mean of the matrix with zero.

import numpy as np
arr = np.random.random_integers(1,10 , size=(4,4)) 
print(arr)


mean = np.mean(arr)
print(mean)

arr[arr < mean] = 0

print(arr)