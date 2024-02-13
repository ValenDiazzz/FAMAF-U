import numpy as np
import matplotlib.pyplot as plt
import math

datos = np.loadtxt("C:/Users/54351/OneDrive/Escritorio/Matemáticas Aplicadas/Análisis Numérico/Datos/covid_italia.csv", delimiter =",", dtype="str")

dates = datos[:, 0]

xc = np.array(range(len(dates))) #days
yc_str = datos[:, 1] #infected
yc = [int(x) for x in yc_str]

yc_ln = np.log(yc)

def grafico_lineal():
    fig, ax= plt.subplots()
    x = np.linspace(0, 42, 400)
    a, b = np.polyfit(xc, yc_ln, 1)

    plt.plot(x, (a*x) + b,color="black", label="aproximación linealizada")
    plt.plot(xc, yc_ln,"o",color="green",label="Datos lineales")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend() 
    plt.show()

def grafico_exponencial():
    fig, ax= plt.subplots()
    x = np.linspace(0, 42, 400)
    a, b = np.polyfit(xc, yc_ln, 1)
    b = np.exp(b)

    plt.plot(x, b*(np.exp(a*x)),color="black", label="aproximación")
    plt.plot(xc, yc,"o",color="green",label="Datos")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend() 
    plt.show()

grafico_lineal()
grafico_exponencial()


