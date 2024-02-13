import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad 
#quad recibe funcion, limites de integracion y devuelve tupla con el valor de la integral y su error absoluto estimativo
def g1(x):
    return np.exp(-(x**2))

def g2(x):
    return (x**2)*np.log(x + ((x**2)+1)**0.5)

print("a) ={}".format(quad(g1, -np.inf, np.inf)[0]))
print("b) ={}".format(quad(g2, 0, 2)[0]))

