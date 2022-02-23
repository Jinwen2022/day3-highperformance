# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 6
# NxN matrix
def matrix_1(N):
    X = np.random.rand(N, N)
    return X
# Nx(N+1) matrix
def matrix_2(N):
    Y = np.random.rand(N,N+1)
    return Y


# result is Nx(N+1)
def getresult(N):
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

def matrixMultiply(N):
# iterate through rows of X
    X = matrix_1(N);
    Y = matrix_2(N);
    result = np.dot(X,Y)
    print(result)

matrixMultiply(N)
