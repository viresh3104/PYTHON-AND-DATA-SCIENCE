# Dot Product: Write a function to calculate the dot product of two 1D arrays.

import numpy as np

def dot_product(arr_1,arr_2):
    dot_product = np.dot(arr_1 , arr_2)
    return dot_product


arr_1 = np.random.random_integers(1,20,5)
arr_2 = np.random.random_integers(1,20,5)
print(arr_2)
print(arr_1)

print(dot_product(arr_1,arr_2))