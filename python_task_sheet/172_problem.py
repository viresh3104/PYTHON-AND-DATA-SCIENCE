# Trace of a Matrix: Write a function to calculate the trace (sum of diagonal elements) of a square matrix.

import numpy as np
def digonal_sum(mat):
    y = np.diagonal(mat)
    print("diagonal elements are :: ",y)
    x = np.trace(mat)
    return x



mat = np.random.randint(1,20,size=(3,3))
print("Matrix is :: \n",mat)
print("sum of diagonal elements are:: ",digonal_sum(mat))