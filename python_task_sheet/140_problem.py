#Implement a program that performs element-wise multiplication of two NumPy arrays without using the numpy.multiply function.

import numpy as np

def muliply(a,b):
    return a*b

a = np.random.random_integers(1,10,3)
b = np.random.random_integers(1,10,3)

print("first array ::", a ,"\nsecond array :: ", b)
print("after multiplication:: ",muliply(a,b))


