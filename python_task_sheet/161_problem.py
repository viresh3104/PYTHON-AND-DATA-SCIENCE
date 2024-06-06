# Sum of Elements: Write a function to calculate the sum of all elements in a 2D array.
import numpy as np
def sum_of_all_element(mat):
    mat = np.sum(mat)
    return mat


mat_1 = np.random.randint(1,20 , size=(3,3))
print(mat_1)
print("sum is :: ",sum_of_all_element(mat_1))