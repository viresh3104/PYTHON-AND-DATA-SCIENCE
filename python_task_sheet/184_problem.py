# Implement a program that performs matrix transposition of a randomly generated NumPy array.

import numpy as np
def transpose(mat):
    mat_transpose = np.transpose(mat)
    return mat_transpose


matrix = np.random.randint(1,20 , size=(3,3))
print(f"transpose of this \n{matrix} is :: \n",transpose(matrix))