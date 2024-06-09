# Given a 1D array, find the difference between each pair of consecutive elements.

import numpy as np
array = np.random.random_integers(1,10,5)
differences = np.diff(array)

print("Original Array:")
print(array)



print("\nDifferences between each pair of consecutive elements:")
print(differences)
