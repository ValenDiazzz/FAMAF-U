import math
import matplotlib.pyplot as plt
from PrimerParcialEj1 import serie_seno


def puntos_x_y(): #Creo la listas con los valores de x equidistantes y sus respectivas imágenes
    hx = []
    hy = []
    x = 0
    for i in range(640):
        hx.append(x)
        x = x + 0.01
        hy.append(serie_seno(x))
    return hx, hy

hx = puntos_x_y()[0]
hy = puntos_x_y()[1]

fig, ax = plt.subplots()
ax.plot(hx, hy,'-.', label="Funcion Seno")

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Aproximación por polinomio de Taylor de orden 4")
plt.legend()
plt.show()

