import matplotlib.pyplot as plt
import numpy as np

#a
x1 = np.linspace(0, 1, 50)
x2 = np.linspace(0, 4*np.pi, 50)
#b
y1 = np.arcsin(x1)
y2 = np.cos(x2)

def grafico_a():
    fig, ax= plt.subplots()
    x = np.linspace(0, 1, 400)
    for i in range(6):
        coeficientes = np.polyfit(x1, y1, i) #Lista con a0 y a1 de cuadrados minimos de grado i.
        fx = np.polyval(coeficientes, x) #Valua el polinomio de grado 1 en los puntos x1

        plt.plot(x, fx,color="black", label="aproximación")
        plt.plot(x1, y1,"o",color="red",label="Datos")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")

        ax.legend() 
        plt.show()

def grafico_b():
    fig, ax= plt.subplots()
    x = np.linspace(0, 4*np.pi, 400)
    for i in range(6): #Cada grafico es de grado i
        coeficientes = np.polyfit(x2, y2, i) #Lista con a0 y a1 de cuadrados minimos de grado i.
        fx = np.polyval(coeficientes, x) #Valua el polinomio de grado 1 en los puntos x1

        plt.plot(x, fx,color="black", label="aproximación")
        plt.plot(x2, y2,"o",color="red",label="Datos")
        ax.set_xlabel("Eje X")
        ax.set_ylabel("Eje Y")

        ax.legend() 
        plt.show()

#Ejecuciones
grafico_a()
grafico_b()