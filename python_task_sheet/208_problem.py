# Create a 4x4 matrix with random values and replace the elements above the main diagonal with their negative value.

import numpy as np

arr = np.random.random_integers(1,10,size=(4,4))
print(arr)

arr[np.triu_indices(4 , k=1)] *= -1
print(arr)
