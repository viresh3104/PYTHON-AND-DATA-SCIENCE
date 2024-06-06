# Matrix Multiplication: Write a function to perform matrix multiplication on two 2D arrays.

import numpy as np

def matrix_multiply(mat_1 , mat_2):
    multiplication = np.matmul(mat_1 ,mat_2)
    return multiplication



mat_1 = np.random.randint(1,20 , size=(3,3))
mat_2 = np.random.randint(1,20,  size=(3,3))
print("First matrix is :: \n",mat_1)
print("Second matrix is ::\n", mat_2)
print("Multiplication of these matrix is :: \n",matrix_multiply(mat_1,mat_2))