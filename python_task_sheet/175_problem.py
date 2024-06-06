# Matrix Inverse: Write a function to calculate the inverse of a square matrix.

import numpy as np
def inverse(mat):
    mat = np.linalg.inv(mat)
    return mat


mat = np.random.randint(1,20,size=(2,2))
print("original matrix is \n",mat)
print("inverse is ::\n",inverse(mat))