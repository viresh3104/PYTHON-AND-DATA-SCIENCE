# Element-wise Subtraction: Write a function to subtract one array from another element-wise
import numpy as np
def element_wise_sub(mat_1 , mat_2):
    mat = np.subtract(mat_1,mat_2)
    return mat




mat_1 = np.random.randint(1,20 , size=(3,3))
mat_2 = np.random.randint(1,20,  size=(3,3))
print("First matrix is :: \n",mat_1)
print("Second matrix is ::\n", mat_2)
print("subtraction of these matrix is :: \n",element_wise_sub(mat_1,mat_2))