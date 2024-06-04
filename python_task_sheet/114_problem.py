# Implement a program that generates a NumPy array with numbers from 0 to 9 and reshapes it into a 3x3 matrix. 


import numpy as np

arr = np.arange(0,9)
arr = arr.reshape(3,3)
print(arr)