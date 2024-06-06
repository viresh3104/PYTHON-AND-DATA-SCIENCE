# Diagonal Elements: Write a function to extract the diagonal elements of a 2D array.

import numpy as np
def digonal(mat):
    mat = np.diagonal(mat)
    return mat


mat = np.random.randint(1,20,size=(3,3))
print(mat)
print(digonal(mat))