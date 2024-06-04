# Create a program that generates a 2D NumPy array with random integers and then flattens it into a 1D array.
import numpy as np
arr = np.random.random_integers(1,10,9)
arr = arr.reshape(3,3)
print("2d array :: \n",arr)

array = arr.flatten()
print("1d flatten array :: \n",array)