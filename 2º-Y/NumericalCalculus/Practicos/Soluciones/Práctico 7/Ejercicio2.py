from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

v_c= np.array([-1, -1], dtype="float")
A = np.array([
    [50, 24],
    [30, 33]
], dtype="float")
b = np.array([2400, 2100], dtype="float")
res = optimize.linprog(c=v_c, A_ub=A, b_ub=b).x #optimize.linprog te devuelve un objeto con varias cosa, .x es un metodo q te da la resolucion

x = np.linspace(0, 50, 100)
y1 = 100 - 25/12 * x
y2 = 2100/33 - 30/33 * x
curva_region = np.minimum(y1, y2)
plt.plot(x, y1, color="red")
plt.plot(x, y2, color="black")
print(res)
plt.plot(res[0], res[1], "*")
plt.xlim([0, 50])
plt.ylim([0, 120])
plt.fill_between(x, curva_region, 3, alpha=0.8) #Alpha es la claridad del color de la region
plt.show()