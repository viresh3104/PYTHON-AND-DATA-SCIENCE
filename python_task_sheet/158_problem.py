# Element-wise Multiplication: Write a function to multiply two arrays element-wise.
import numpy as np
def multiply(arr_1, arr_2):
    arr_3 = np.multiply(arr_1,arr_2)
    return arr_3


arr_1 = np.random.randint(1,10,5)
arr_2 = np.random.randint(1,10,5)
print(arr_1)
print(arr_2)
print(multiply(arr_1 ,arr_2))