import numpy as np

Asup = np.array([
    [1, 2, 0], 
    [0, 3, 1], 
    [0, 0, 5]
    ]) 
b1 = np.array([11, 17, 10]) #sol:(1, 5, 2)

Ainf = np.array([
    [1, 0, 0], 
    [0, 2, 0], 
    [0, 0, 1]
    ]) 
b2 = np.array([1, 6, 6])

def soltrsup(A, b):    
    assert np.prod(np.diag(A)) != 0,"Error: la matriz es singular"
    n = len(A)-1
    x = [b[n]/A[n, n]]
    for i in range(n-1, -1, -1):
        sum = 0
        idx = 0      
        for j in range(n, i, -1):
            sum =  sum + A[i,j]*x[idx]
            idx+= 1
        x.append((b[i]-sum)/A[i,i])
    x.reverse()
    return x

def soltrinf(A, b):    
    assert np.prod(np.diag(A)) != 0,"Error: la matriz es singular"
    n = len(A)-1
    x = [b[0]/A[0, 0]]
    for i in range(1, n+1):
        sum = 0
        for j in range(0, i):
            sum = sum + A[i, j]*x[j]
        x.append((b[i]-sum)/A[i,i])
    return x
