# Implement a program that generates a random NumPy array and finds the maximum and minimum values.

import numpy as np

x = np.random.random_integers(1,100,15)
print(x)

max = np.max(x)
min = np.min(x)
print("max value is :: ",max)
print("min value is ::",min)