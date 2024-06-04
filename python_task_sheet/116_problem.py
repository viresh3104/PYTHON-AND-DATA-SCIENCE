#  Create a function that takes a list of numbers and returns the NumPy array sorted in ascending order.
import numpy as np

def sort_array(data):
    num_arr = np.array(data, dtype=float)
    sorted_arr = np.sort(num_arr)
    return sorted_arr




# Example usage
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_arr = sort_array(data)
print("Sorted array:", sorted_arr)
