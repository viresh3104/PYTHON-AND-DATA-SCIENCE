# Create a 3x3 identity matrix and convert its diagonal elements to the square of the respective indices (0, 1, 2).

import numpy as np

arr = np.eye(3)
size = arr.shape[0]
for i in range(size):
    arr[i, i] = i**2

print(arr)