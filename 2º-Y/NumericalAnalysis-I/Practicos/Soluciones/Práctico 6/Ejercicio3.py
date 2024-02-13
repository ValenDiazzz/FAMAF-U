import numpy as np
from scipy.linalg import lu
from Ejercicio1 import soltrinf, soltrsup
A = np.array([
    [2, -2, 1],
    [1, 1, 3],
    [0, 4, 1]
])
b = np.array([-1, 6, 9])
def sollu(A, b):
    P, L, U = lu(A) #La inversa de P es P.
    b = P@b  #@ hace la multiplicacion matricial.
    y = soltrinf(L, b)
    x = soltrsup(U, y)
    return x

