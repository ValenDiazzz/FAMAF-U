import numpy as np
from Ejercicio2 import soleg
from Ejercicio3 import sollu
A=np.array([
    [4, -1, 0, -1, 0, 0], 
    [-1, 4, -1, 0, -1, 0],
    [0, -1, 4, 0, 0, -1],
    [-1, 0, 0, 4, -1, 0],
    [0, -1, 0, -1, 4, -1],
    [0, 0, -1, 0, -1, 4]
])
b1 = np.array([1, 1, 1, 0, 0, 0])
b2 = np.array([1, 1, 1, 1, 1, 1])

print("b1, sollu:{}".format(sollu(A, b1)))
print("b1, soleg:{}".format(soleg(A,b1)))
print("b2, sollu:{}".format(sollu(A, b2)))
print("b2, soleg:{}".format(soleg(A,b1)))