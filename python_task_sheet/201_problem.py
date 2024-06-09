# Create a 1D array of 10 random numbers. Find and print the cumulative sum of the elements.

import numpy as np

arr = np.random.random_integers(1,20,10)
print(arr)
sum_c = []
for i in range(len(arr)):
    sum_c.append(sum(arr[:i+1]))

print(sum_c)