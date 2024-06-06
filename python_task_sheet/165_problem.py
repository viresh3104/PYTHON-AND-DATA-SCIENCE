# Element-wise Division: Write a function to divide one array by another element-wise.
import numpy as np
def division(mat_1,mat_2):
    mat = np.divide(mat_1,mat_2)
    return mat




mat_1 = np.random.randint(1,20 , size=(3,3))
mat_2 = np.random.randint(1,20,  size=(3,3))
print("First matrix is :: \n",mat_1)
print("Second matrix is ::\n", mat_2)
print("division of these matrix is :: \n",division(mat_1,mat_2))