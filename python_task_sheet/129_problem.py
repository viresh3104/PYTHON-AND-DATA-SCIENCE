# 4. Write a program that reads a CSV file containing student names and their scores.
# Calculate and print the average score using NumPy.


import numpy as np
import pandas as pd

arr = pd.read_csv("students.csv")
arr = np.mean(arr["Total Score"])
print(arr)