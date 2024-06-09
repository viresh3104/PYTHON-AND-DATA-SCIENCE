# Create a 6x6 matrix and fill it with a checkerboard pattern (alternating 0s and 1s).
import numpy as np
arr = np.zeros((6,6))
print(arr)
print("*"*50)
print("*"*50)

arr[1::2, ::2] = 1  
arr[::2, 1::2] = 1  

print(arr)