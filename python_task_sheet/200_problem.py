# Create a 3x3 matrix with values ranging from 1 to 9 and rotate the matrix 90 degrees clockwise.

import numpy as np

arr = np.random.random_integers(1,9 , size=(3,3))
print(arr)

arr = np.rot90(arr)
print(arr)