# Implement a function that takes a NumPy array and normalizes it to have zero mean and unit variance.
import numpy as np
arr = np.random.random_integers(1,10,5)
print(arr)
mean = np.mean(arr)
varience = np.std(arr)
x = (arr - mean) / varience
print(x)




# not understood the concept of zero mean and unit varience

