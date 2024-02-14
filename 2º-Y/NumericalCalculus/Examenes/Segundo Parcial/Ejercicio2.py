import numpy as np
import matplotlib.pyplot as plt

x = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]

def graficar_puntos():
    fig, ax= plt.subplots()
    plt.plot(x, y,"o",color="yellow",label="Datos")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.legend() 
    plt.show()


def trapecio_adaptativo(x, y):
    sumatoria = 0
    for i in range(len(x)-1):
        sumatoria = sumatoria + (x[i+1]-x[i])/2 * (y[i+1] + y[i])
    return sumatoria


metros_a_remover = trapecio_adaptativo(x, y)*10

#Ejecuciones
graficar_puntos()
print("La integral aproximada es:", trapecio_adaptativo(x, y))
print("Los metros de tierra a remover son",metros_a_remover)