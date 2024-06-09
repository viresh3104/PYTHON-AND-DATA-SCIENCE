# Create a 4x4 matrix with random integers and replace the diagonal elements with the sum of their row.

import numpy as np

matrix = np.random.randint(1,16, size=(4,4))
print("this is matrix :: \n",matrix)

diagonal_sum = list(np.sum(matrix , axis=1))
print("this is sum of rows ::  ",diagonal_sum)


for i in range(matrix.shape[0]):
    row_sum = np.sum(matrix[i, :])
    matrix[i, i] = row_sum
print("this is the changed matrix:: \n",matrix)
