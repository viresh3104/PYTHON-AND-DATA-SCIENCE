# Write a function that computes the element-wise square root of a NumPy array without using the numpy.sqrt function. 
import numpy as np

def square_root(arr):
    return arr ** 0.5



arr = np.array([1, 4, 9, 16, 25 , 49])
sqrt_arr = square_root(arr)
print(sqrt_arr) 
