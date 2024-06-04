# Write a function that calculates the Euclidean distance between two
#  points represented as NumPy arrays in n-dimensional space.
import numpy as np
def euclidien_dist(point_1,point_2):
    return np.sqrt(np.sum((point_1-point_2)) **2)

a = np.random.random_integers(1,10,3)
b = np.arange(1,10,3)
print(a)
print(b)
print("Eculidian distance:: ",euclidien_dist(a,b))




