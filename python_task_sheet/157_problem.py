# Element-wise Addition: Write a function to add two arrays element-wise.

import numpy as np

def add(arr_1 ,arr_2):
    arr_3 = np.add(arr_1 ,arr_2)
    print("this is addition of two array:: ",arr_3)



arr_1 = np.random.random_integers(1,10,5)
arr_2 = np.random.random_integers(1,10,5)
print(arr_1)
print(arr_2)
print(add(arr_1 ,arr_2))