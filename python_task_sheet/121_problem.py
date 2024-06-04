# Create a program that uses NumPy to calculate the inverse of a 2×2 matrix
import numpy as np
def inverse_mat(matrix):
    num_arr = np.array(matrix)
    inverse = np.linalg.inv(num_arr)
    return inverse




matrix = [
    [1, 2],
    [3, 4]
]
inverse = inverse_mat(matrix)
print("Inverse of the matrix: \n", inverse)