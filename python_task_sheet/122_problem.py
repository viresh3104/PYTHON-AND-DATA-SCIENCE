# Implement a function that takes a NumPy array and returns the transpose of the array

import numpy as np

def transpose_array(arr):
    transposed_arr = np.transpose(arr)
    return transposed_arr

# Example usage
arr = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("original array :: ",arr)
transposed_arr = transpose_array(arr)
print("Transposed array: \n", transposed_arr)
