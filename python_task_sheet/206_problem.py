# Create a 6x6 matrix with random values and calculate the sum of the elements in the secondary diagonal (bottom-left to top-right).

import numpy as np

arr = np.random.random_integers(1,10,size=(6,6))
print(arr)


secondary_diagonal = np.diag(arr[::-1])                        
sum_of_this_diagonal = np.sum(secondary_diagonal)

print(sum_of_this_diagonal)
