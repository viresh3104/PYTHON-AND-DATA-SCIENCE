# Given a 1D array, normalize the array (i.e., scale the values such that the maximum value is 1 and the minimum value is 0).
import numpy as np
arr = np.random.randint(1,10+1,5)
print(arr)

min_value = np.min(arr)
max_value = np.max(arr)

normalized_arr = (arr - min_value) / (max_value - min_value)

print(normalized_arr)