# Create a 5x5 matrix and set the elements in the border to 1 and the rest to 0.


import numpy as np

arr = np.zeros((5,5))
# print(arr)

arr[0, 0:5 ] = 1      #top
arr[-1 , :]  = 1      #bottom
arr[1:4 , 4]  =1      #right
arr[1:4 ,0]  =1      #left

print(arr)