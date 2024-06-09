# Given two 1D arrays, find the common elements between them.

import numpy as np

arr = np.random.random_integers(1,10,8)
arr_2 = np.random.random_integers(1,10,8)

sorted_arr = np.intersect1d(arr,arr_2)
print(arr ,"\n", arr_2,"\n" , sorted_arr)