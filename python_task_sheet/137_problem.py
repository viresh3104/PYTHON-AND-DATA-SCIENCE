# Eigenvalues and Eigenvectors Find the eigenvalues and corresponding eigenvectors of a given square matrix using NumPy.

import numpy as np


def eigenvalues_eigenvectors(matrix):
    values, vectors = np.linalg.eig(matrix)
    return values , vectors


matrix = np.random.random_integers(10,size = (3,3))
print(matrix)
print(eigenvalues_eigenvectors(matrix))
