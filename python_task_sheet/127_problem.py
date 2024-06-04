# Implement a program that calculates the mean squared error (MSE) between two NumPy arrays representing predicted and actual values.
import numpy as np
def mse(actual,predicted):
    return (np.mean(actual - predicted) **2)

actual = np.random.random_integers(1,5,3)
predicted = np.random.random_integers(1,5,3)
print("actual array ::",actual, "predicted array ::",predicted)
print("MSE is :: ",mse(actual,predicted))