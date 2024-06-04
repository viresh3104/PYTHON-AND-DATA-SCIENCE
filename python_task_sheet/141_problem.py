# Create a function that takes a 2D NumPy array as input and returns the indices of the maximum value in each row.
import numpy as np
def maxindex(arr):
    return np.argmax(arr ,axis = 1)

# arr = np.array([[1, 3, 2], [4, 0, 5]])
arr = np.random.random_integers(10,size=(3,3))
print(arr)
print(maxindex(arr))