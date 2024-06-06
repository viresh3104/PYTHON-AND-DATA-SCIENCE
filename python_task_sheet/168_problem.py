# Reshape an Array: Write a function to reshape a 1D array into a 2D array with specified dimensions
import numpy as np
def reshaping_array(arr):
    x = arr.reshape(3,3)
    return x


arr = np.random.random_integers(1,20 ,9)
print(arr)
print(reshaping_array(arr))