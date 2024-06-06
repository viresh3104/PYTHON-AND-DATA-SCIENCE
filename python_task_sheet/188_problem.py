# Implement a program that calculates the element-wise exponential of a NumPy array without using the numpy.exp function.


import numpy as np

def pearson_correlation_coefficient_matrix(arr):
    return np.corrcoef(arr)


if __name__ == "__main__":
    arr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
    correlation_matrix = pearson_correlation_coefficient_matrix(arr)
    print("Pearson correlation coefficient matrix:\n",correlation_matrix)
