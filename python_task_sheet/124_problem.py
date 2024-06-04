# Implement a function that generates a random 5x5 
# NumPy array of integers in the range [0, 10), and then replaces all even numbers with -1. 

import numpy as np

arr = np.random.random_integers(1,11,25)
arr = arr.reshape(5,5)
print(arr)
print("*"*30)
arr[arr % 2 == 0] = 1
print(arr)
