# Matrix Determinant: Write a function to calculate the determinant of a square matrix
import numpy as np
def determinant(mat):
    mat = np.linalg.det(mat)
    return mat


mat = np.random.randint(1,20,size=(2,2))
print(mat)
print(determinant(mat))