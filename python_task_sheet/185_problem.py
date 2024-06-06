# Create a function that takes a NumPy array as input and returns the cumulative sum along a specified axis.

import numpy as np

def cumulative_sum(arr, axis):
    return np.cumsum(arr, axis=axis)


if __name__ == "__main__":
    arr = np.random.randint(1, 10, size=(3, 3))
    print("Original Array:")
    print(arr)
    
    
    cum_sum_axis0 = cumulative_sum(arr, axis=0)
    print("\nCumulative Sum along axis 0 (rows):")
    print(cum_sum_axis0)
    
    
    cum_sum_axis1 = cumulative_sum(arr, axis=1)
    print("\nCumulative Sum along axis 1 (columns):")
    print(cum_sum_axis1)
