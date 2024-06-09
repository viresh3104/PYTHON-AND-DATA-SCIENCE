# Given a 2D array, subtract the mean of each row from the respective row elements.

import numpy as np

arr = np.random.random_integers(1,10,size=(2,2))
print(arr)


mean = np.mean(arr , axis=1)
print(mean)

arr = arr - mean
print(arr)