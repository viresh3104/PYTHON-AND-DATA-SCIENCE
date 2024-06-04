# Create a function that generates a 1D NumPy array containing the Fibonacci sequence up to the 10th term.

import numpy as np
arr = np.zeros(10)
arr[1] = 1
for i in range(2,10):
    arr[i] = arr[i-1] + arr[i-2]
print("fibonacci seq is ::",arr)