# Matrix Multiplication Compute the matrix product of two given matrices A and B using NumPy.
import numpy as np
def matrix_multiplication(A, B):
    return np.dot(A, B)

# Example
arr = np.random.random_integers(10 ,size=(3,3))
arr_2 = np.random.random_integers(10,size=(3,3))
print(arr)
print(arr_2)
print(matrix_multiplication(arr, arr_2))

