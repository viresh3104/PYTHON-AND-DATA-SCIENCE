# Generate a random 5x5 matrix and find the sum of the elements in the lower triangular part of the matrix (including the diagonal).

import numpy as np

arr = np.random.random_integers(1,50 ,size=(5,5))
print(arr)
sum = 0.0
for i in range(5):
    for j in range(i+1):
        sum += arr[i , j]

print(sum)