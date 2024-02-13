import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

v_c= np.array([10, 8], dtype="float")
A = -np.array([
    [3, 2],
    [1, 3],
    [8, 2],
], dtype="float")
b = -np.array([3, 1.5, 4], dtype="float")
res = optimize.linprog(c=v_c, A_ub=A, b_ub=b).x #optimize.linprog te devuelve un objeto con varias cosa, .x es un metodo q te da la resolucion

x = np.linspace(0, 1.5, 100)
y1 = 1.5 - 1.5 * x
y2 = 0.5 - 1/3 * x
y3 = 2 - 4 * x
curva_region = np.maximum(np.maximum(y1, y2), y3)
plt.plot(x, y1, color="red")
plt.plot(x, y2, color="black")
plt.plot(x, y3, color="green")
plt.ylim([-1, 4])
plt.fill_between(x, curva_region, 3, alpha=0.2) #Alpha es la claridad del color de la region
plt.show()