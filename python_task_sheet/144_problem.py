# Write a program that performs matrix multiplication of two randomly generated NumPy arrays.
import numpy as np

def random_matrix_multiplication(shape1, shape2):
    arr1 = np.random.rand(*shape1)
    arr2 = np.random.rand(*shape2)
    print(arr1,arr2)
    return np.dot(arr1, arr2)

print(random_matrix_multiplication((2, 3), (3, 2)))
