# Program to multiply two matrices using nested loops
import numpy as np

N = 250

# NxN matrix
X = np.random.rand(N,N)*100 #Matrix contains floats
X = X.astype(int)
#print(X)

# Nx(N+1) matrix
Y = np.random.rand(N,N+1)*100
Y = Y.astype(int)
#print(Y)

# result is Nx(N+1)
@profile
def matmul(x,y):
    result = np.matmul(x,y)
    return result

print(matmul(X,Y))
