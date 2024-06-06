# Standard Deviation: Write a function to calculate the standard deviation of all elements in a 2D array.
import numpy as np
def standard_dev(mat):
    mat = np.std(mat)
    return mat

mat_1 = np.random.randint(1,20 , size=(3,3))
print(mat_1)
print("standard deviation is :: ",standard_dev(mat_1))