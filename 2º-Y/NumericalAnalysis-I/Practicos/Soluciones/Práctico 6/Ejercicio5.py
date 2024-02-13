import numpy as np

A = np.array([
    [1, 2, -2],
    [1, 1, 1],
    [2, 2, 1]
])
b = np.array([7, 2, 5])

def jacobi(A, b, err, mit):
    M=np.diag(np.diag(A))
    N = M-A
    M_inv = np.diag(1/np.diag(M)) #Pues M es diagonal
    b = np.array(b)
    x0 = np.zeros(b.shape) #x inicial = (0, 0,..., 0)
    x = [x0]
    k = 0
    error = 100
    while k <= mit and error >= err:
        x.append(M_inv @ (N@x[k] + b))
        error = np.linalg.norm(x[k+1]- x[k], ord = np.inf)
        k+=1
    return[x[-1], k]


def gseidel(A, b, err, mit):
    M=np.tril(A)
    N = M-A
    #M_inv =   #Si se completa esto el ej queda resuelto
    b = np.array(b)
    x0 = np.zeros(b.shape) #x inicial = (0, 0,..., 0)
    x = [x0]
    k = 0
    error = 100
    while k <= mit and error >= err:
        x.append(M_inv @ (N@x[k] + b))
        error = np.linalg.norm(x[k+1]- x[k], ord = np.inf)
        k+=1
    return[x[-1], k]
