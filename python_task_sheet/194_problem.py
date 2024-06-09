# Generate a 1D array of 15 random numbers between 0 and 1. Sort the array in descending order without using the built-in sort function.


import numpy as np

arr = np.random.rand(15)
n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]



print(arr)