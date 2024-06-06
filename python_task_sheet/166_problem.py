# Array Slice: Write a function to extract a subarray from a given 2D array based on the specified row and column ranges
import numpy as np
def slicing(mat):
    print("original mat ::\n " , mat)
    mat = mat[:2,1:]
    return mat

mat = np.random.randint(1,20,size=(3,3))
print(slicing(mat))