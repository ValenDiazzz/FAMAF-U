import numpy as np
from Ejercicio1 import soltrsup
A = np.array([
    [1, 2, 0], 
    [0, 3, 1], 
    [1, 2, 5]
])
b = np.array([11, 17, 21]) #sol = (1, 5, 2)

def egauss(A, b):
    n = len(A)-1
    for j in range(n):
        B=A.copy()
        for i in range(j, n):
            if A[j, j]!= 0:
                A[i+1] = A[i+1] - A[j]*(A[i+1, j]/A[j, j])
                b[i+1] = b[i+1] - b[j]*(B[i+1, j]/B[j, j])
    return [A, b]

def soleg(A, b):
    U, y= egauss(A, b)
    return soltrsup(U, y)

#print(soleg(A, b))