# Row-wise Sum: Write a function to calculate the sum of elements for each row in a 2D array.

import numpy as bc
def row_wise_sum(mat):
    mat = bc.sum(mat , axis=1)
    return mat


mat = bc.random.randint(1,20,size=(2,2))
print(mat)
print(row_wise_sum(mat))
