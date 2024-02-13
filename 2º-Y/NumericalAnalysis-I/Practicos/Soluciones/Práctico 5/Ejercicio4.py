import numpy as np
from Ejercicio1 import intenumcomp


def fun_a(x):
    return x*np.exp(-x)
def fun_b(x):
    return x*np.sin(x)
def fun_c(x):
    return (1+(x**2))**(3/2)

#probamos un 1 intervalo, luego con 2.. y así. Si el valor de la integral difiere en algo menor que 10^-5 entonces decimos que ese es el resultado

funciones = [fun_a, fun_b, fun_c]
integrals = [] #integral calculado por simpson
integralt = [] #integral calculado por trapecio


for f in funciones:
    n=1
    error1 = 1
    error2 = 1
    while error1 >= 1e-5:
        integrals_k = intenumcomp(f, 0, 1, n, "simpson")
        integrals_k_1 = intenumcomp(f, 0, 1, n+1, "simpson")
        error1 = abs(integrals_k) - abs(integrals_k_1)
        n+=1
    integrals.append(integrals_k_1)
    while error2 >= 1e-5:
        integralt_k = intenumcomp(f, 0, 1, n, "trapecio")
        integralt_k_1 = intenumcomp(f, 0, 1, n+1, "trapecio")
        error2 = abs(integralt_k) - abs(integralt_k_1)
        n+=1
    integralt.append(integralt_k_1)

#print(integrals, integralt)