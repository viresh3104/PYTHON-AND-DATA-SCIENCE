# Create a function that takes a NumPy array as input and returns the indices of the non-zero elements.
import numpy as np
def nonzero(array):
    array = np.nonzero(array)
    return array


b = np.array([0, 1, 2, 0, 3])
print(b)
print(nonzero(b))
