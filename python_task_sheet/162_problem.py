# Mean of Elements: Write a function to calculate the mean of all elements in a 2D array.
import numpy as np
def mean(mat):
    mat = np.mean(mat)
    return mat


mat_1 = np.random.randint(1,20 , size=(3,3))
print(mat_1)
print("mean is :: ",mean(mat_1))