# Write a function that computes the dot product between two 1D NumPy arrays without using the numpy.dot function

import numpy as np

arr_1 = np.random.random_integers(1,10,5)
arr_2 = np.random.random_integers(1,10,5)

x = np.sum(arr_1 * arr_2)
print("1st array:: \n",arr_1 ,"\n2nd array ::\n",arr_2)
print(x)

