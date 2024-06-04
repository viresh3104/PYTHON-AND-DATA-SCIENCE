# Implement a program that calculates the determinant of a square matrix using NumPy.
import numpy as np

def det_mat(matrix):
    return np.linalg.det(matrix)



arr = np.random.random_integers(10,size=(3,3))
print(arr)
print(det_mat(arr))