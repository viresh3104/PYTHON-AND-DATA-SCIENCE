# Implement a program that calculates the cross product of two 3D NumPy arrays representing vectors. 

import numpy as np


np.random.seed(42)
vec1 = np.random.rand(3)
vec2 = np.random.rand(3)


print("Vector 1:")
print(vec1)
print("\nVector 2:")
print(vec2)

result = np.cross(vec1, vec2)


print("\nCross Product of Vector 1 and Vector 2:")
print(result)



# By setting the seed to a specific value (in this case, 42), you ensure that the
# sequence of random numbers generated is the same every time you run the program. This is useful for reproducibility, 
# allowing you to get consistent results each time the code is executed. 