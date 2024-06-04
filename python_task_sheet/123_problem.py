# Write a Python program that takes two NumPy arrays of 
# the same shape and calculates their element-wise sum, difference, and product. 

import numpy as np

def element_wise_operations(arr1, arr2):
    sum_arr = np.add(arr1, arr2)
    diff_arr = np.subtract(arr1, arr2)
    prod_arr = np.multiply(arr1, arr2)
    return sum_arr, diff_arr, prod_arr

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
sum_arr, diff_arr, prod_arr = element_wise_operations(arr1, arr2)
print("Element-wise sum:", sum_arr)
print("Element-wise difference:", diff_arr)
print("Element-wise product:", prod_arr)
