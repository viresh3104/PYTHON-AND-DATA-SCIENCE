# Column-wise Sum: Write a function to calculate the sum of elements for each column in a 2D array.

import numpy as np
def coloum(mat):
    mat = np.sum(mat , axis=0)
    return mat


mat = np.random.randint(1,20,size=(3,3))
print(mat)
print(coloum(mat))
