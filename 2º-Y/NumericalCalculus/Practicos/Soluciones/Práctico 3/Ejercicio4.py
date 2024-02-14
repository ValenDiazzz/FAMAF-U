#from Ejercicio2 import inewton, dif_divididas
from Ejercicio2 import inewton
import matplotlib.pyplot as plt
import numpy as np
from math import pi, cos

fig, ax= plt.subplots() 

def f(x):
    return 1/(1+ (25*(x**2)))

#(x,y) de f
x1 = np.linspace(-1, 1, 200) # puntos equidistantes
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Ejercicio 4")

for i in range(1, 16):
    x2 = np.arange(1, (i+1)+1) #i+1 = n+1, le sumamos otro 1 porq el arange le quita uno al final, como el range
    x2 = ((2*(x2-1)) / i) - 1
    y2 = f(x2)

    y_pol_interpolant2 = inewton(x2, y2, x1)
    
    plt.plot(x1, y_pol_interpolant2, label="aproximacion")
    plt.plot(x1, f(x1), label="f(x)")

    plt.legend()
    plt.show()
    
