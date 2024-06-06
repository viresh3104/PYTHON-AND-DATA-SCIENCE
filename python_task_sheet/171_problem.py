# Lower Triangular Matrix: Write a function to create a lower triangular matrix from a given 2D array.

import numpy as np
def upper_tri_mat(mat):
    mat = np.tril(mat)
    return mat



mat = np.random.randint(1,20,size=(3,3))
print(mat)
print(upper_tri_mat(mat))