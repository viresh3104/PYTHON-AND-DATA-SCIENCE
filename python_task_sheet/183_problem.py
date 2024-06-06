# Develop a function that takes a NumPy array as input and returns the indices of the local minima 
# (values smaller than both of their neighbors).
import numpy as np
def minima(arr):
    list_to_store_element = []

    for i in range(1,len(arr)-1):
        if arr[i] < arr[i-1] and arr[i] < arr [i+1]:
            list_to_store_element.append(i)
    return list_to_store_element

arr = np.random.random_integers(1,20,15)
print(arr)
print(minima(arr))

