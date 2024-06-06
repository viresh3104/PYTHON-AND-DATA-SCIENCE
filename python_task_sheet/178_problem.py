# Element-wise Exponential: Write a function to raise each element in a 2D array to the power of a specified value

import numpy as np

def expo(mat , power):
    return np.power(mat , power)


mat = np.random.randint(1,10,size=(2,2))
print(mat)
power = 2
print(expo(mat , power))