import numpy as np
import matplotlib.pyplot as plt
from numpy import ndarray
from scipy import linalg

def egauss(A: ndarray, b: ndarray):
    n = len(b)
    y = np.copy(b)
    U = np.copy(A)

    for k in range(0, n): # por cada pivot
        for i in range(k+1, n): # por cada fila abajo del pivot
            if(U[k, k] == 0):
                raise Exception("Un pivote quedó 0, no se puede seguir")
            m = U[i, k] / U[k, k]
            for j in range(0, n): # por cada elemento de la fila a la derecha de la diagonal(inclusive)
                if j < k+1:
                    U[i, j] = 0
                else:
                    U[i, j] = U[i, j] - m*U[k, j]
            y[i] = y[i] - m*y[k]

    return (U, y)

def soltrinf(A: ndarray, b: ndarray) -> ndarray:
    n = len(b)
    sol = np.zeros(n)
    for i in range(0, n):
        sumc = 0 # Variable para sumar los coeficientes por las partes de la solucion que ya saque
        for j in range(0, i):
            sumc += sol[j] * A[i, j]
        sol[i] = ((b[i] - sumc)/A[i, i])
    return sol

def soleg(A: ndarray, b:ndarray):
    U, y = egauss(A, b)
    B = np.flip(A, 0)
    return soltrinf(B, b)

# sum(f(x)-Y(x))2

# a x2 + b x  + c 1     = y 
# a x3 + b x2 + c x     = y x
# a x4 + b x3 + c x2    = y x2

def ajuste_cuad(x,y):
    m = len(x)
    #hago las sumatorias
    sum_x = np.dot(x, np.ones(m))
    sum_x_2 = sum(x**2)
    sum_x_3 = sum(x**3)
    sum_x_4 = sum(x**4)

    sum_y = np.dot(y, np.ones(m))
    sum_xy = np.dot(x, y)
    sum_xy2 = np.dot((x**2), y)

    #retorno la funcion armada con mis a y que sea valuable con un v
    
    ecu = np.array([  
    [sum_x_2, sum_x,   m],
    [sum_x_3, sum_x_2, sum_x],
    [sum_x_4, sum_x_3, sum_x_2],       
                    ])

    vect = np.array([sum_y, sum_xy, sum_xy2])

    # estan todos bien, comprobados con calcu
    # print("\n")
    # print(f"m: es: {m}")
    # print(f"sum_x: es: {sum_x}")
    # print(f"sum_x_2: es: {sum_x_2}")
    # print(f"sum_x_3: es: {sum_x_3}")
    # print(f"sum_x_4: es: {sum_x_4}")
    # print(f"sum_y: es: {sum_y}")
    # print(f"sum_xy: es: {sum_xy}")
    # print(f"sum_xy2: es: {sum_xy2}")
    # print("\n")

    
    # coef = soleg(ecu, vect)
    coef = linalg.solve(ecu,vect)
    

    a = coef[0]
    b = coef[1]
    c = coef[2]

    # print("\n")
    # print(f"a: es: {a}")
    # print(f"b: es: {b}")
    # print(f"c: es: {c}")
    # print("\n")

    return lambda v:(a*(v**2)+b*v+c)


# tabla de datos 
xs = np.array([-2,0,2,4])
ys = np.array([0,-2,1,2])

# para comprobar

# polyfit retorna los coeficientes 
# poly1d construye el polinomio
ajuste = np.poly1d(np.polyfit(xs, ys, 2)) 
# no se puede polyfit

# ajuste = ajuste_cuad(xs,ys)

mat_ecu = np.array([ 
    
    [ajuste(5), 1, 1],
    [1, ajuste(5), 1],
    [1, 1, ajuste(5)],
                        
                    ])

vec_ecu = np.array([1, 1, 1])

print("\n")
print(f"f(5)= {ajuste(5)}")
print("\n")

coef = soleg(mat_ecu, vec_ecu)

print("La terna (x,y,z) que resuelve el sistema de ecuaciones es")
print(f" x = {coef[0]}")
print(f" y = {coef[1]}")
print(f" z = {coef[2]}")
