#  Write a Python program that uses NumPy to find the mean, median, and standard deviation of a dataset. 
import numpy as np


def statictics(data):
    num_arr = np.array(data)
    mean_value = np.mean(num_arr)
    median_value = np.median(num_arr)
    std_dev = np.std(num_arr)
    return mean_value , median_value , std_dev


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean_value, median_value, std_dev_value = statictics(data)

print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_dev_value}")