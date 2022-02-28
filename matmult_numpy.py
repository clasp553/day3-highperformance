# Program to multiply two matrices using nested loops
import numpy as np

N = 250

# NxN matrix
X = np.random.rand(N,N)*100
X = X.astype(int)

# Nx(N+1) matrix
Y = np.random.rand(N,N)*100
Y = Y.astype(int)

# result is Nx(N+1)
@profile
def matmul(mat1,mat2):
    result = np.matmul(mat1,mat2)
    return result

print(matmul(X,Y))
