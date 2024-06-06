# Develop a function that takes a NumPy array as input and returns the indices of the sorted elements in descending order.

import numpy as np

def sorted_indices_descending(arr):
    return np.argsort(arr)[::-1]


# [::-1] used to sorting in decending order


arr = np.random.random_integers(1,20,10)
print(arr)
sorted_indices = sorted_indices_descending(arr)
print("Indices of sorted elements in descending order:", sorted_indices)
