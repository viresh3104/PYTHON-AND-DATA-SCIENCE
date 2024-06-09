# Create a 5x5 matrix with random values and replace all the elements greater than a given threshold with the threshold value.
import numpy as np
arr = np.random.randint(1,50,size=(5,5))
print(arr)
x = int(input("ENter the value :: "))
arr = np.where(arr > x , x , arr)
print(arr)