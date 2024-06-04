# Broadcasting Given a 2D array and a 1D array, add the 1D array to each row of the 2D array using broadcasting.
import numpy as np
def broadcast_addition(arr2D, arr1D):
    return arr2D + arr1D

# Example
x = np.arange(1,10)
arr2D = x.reshape(3,3)
print(arr2D)


arr1d = np.arange(1,4)
print(arr1d)


print(broadcast_addition(arr2D, arr1d))
