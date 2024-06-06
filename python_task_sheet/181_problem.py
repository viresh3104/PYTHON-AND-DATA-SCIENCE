# Create a function that takes a NumPy array as input and returns a new array with only the unique elements sorted in ascending order. 
import numpy as np
def unique_ele(arr):
    s_arr = np.sort(arr)
    u_arr = np.unique(s_arr)
    return u_arr



arr = np.random.random_integers(1,20,15)
print(arr)
print(unique_ele(arr))