# Flattening an Array: Write a function to convert a 2D array into a 1D array (flattening the array).

import numpy as np
def flat(mat):
    mat = np.ndarray.flatten(mat)
    return mat


mat = np.random.randint(1,20,  size=(3,3))
print("First matrix is :: \n",mat)
print(flat(mat))