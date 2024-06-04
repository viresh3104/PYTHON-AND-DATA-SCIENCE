# Create a function that takes two NumPy arrays as input and concatenates them horizontally (side by side).

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])


x = np.hstack((arr1,arr2))
print(x)