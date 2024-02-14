import numpy as np
import matplotlib.pyplot as plt
import math

#datos
datos_a = np.loadtxt("C:/Users/54351/OneDrive/Escritorio/Matemáticas Aplicadas/Análisis Numérico/Datos/datos3a.txt")
xc = datos_a[0]
yc = datos_a[1]

xc_a = np.log(xc)
yc_a = np.log(yc)

datos_b =np.loadtxt("C:/Users/54351/OneDrive/Escritorio/Matemáticas Aplicadas/Análisis Numérico/Datos/datos3b.txt")

xcc = datos_b[0]
ycc = datos_b[1]
xcc_b = xcc   #x/y = Ax + b
ycc_b = xcc / ycc

#Gráficos
def grafico_a_lineal():
    fig, ax= plt.subplots()

    x = np.linspace(np.log(1), np.log(5), 400)
    a, b = np.polyfit(xc_a, yc_a, 1) #Lista con a0 y a1 de cuadrados minimos de grado i.
    fx = np.polyval(np.array([a,b]), x) #Valua el polinomio de grado 1 en los puntos x1
    
    plt.plot(x, fx,color="black", label="aproximación linealizada")
    plt.plot(xc_a, yc_a,"o",color="green",label="Datos lineales")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend() 
    plt.show()

def grafico_a_general():
    fig, ax= plt.subplots()

    x = np.linspace(1, 5, 400)
    a, b = np.polyfit(xc_a, yc_a, 1) #Lista con a0 y a1 de cuadrados minimos de grado i.
    

    plt.plot(x,(math.e**b) * (x**a) ,color="black", label="aproximación")
    plt.plot(xc, yc,"o",color="green",label="Datos")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend() 
    plt.show()

def grafico_b_lineal():  
    fig, ax= plt.subplots()

    x = np.linspace(1e-15, 20, 400)
    a, b = np.polyfit(xcc_b, ycc_b, 1) #Lista con a0 y a1 de cuadrados minimos de grado i.
    fx = np.polyval(np.array([a,b]), x) #Valua el polinomio de grado 1 en los puntos x1
    
    plt.plot(x, fx,color="black", label="aproximación linealizada")
    plt.plot(xcc_b, ycc_b,"o",color="green",label="Datos lineales")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend() 
    plt.show()

def grafico_b_general():
    fig, ax= plt.subplots()

    x = np.linspace(1e-15, 20, 400)
    a, b = np.polyfit(xcc_b, ycc_b, 1) #Lista con a0 y a1 de cuadrados minimos de grado i.
    

    plt.plot(x, x/(a*x + b)  ,color="black", label="aproximación")
    plt.plot(xcc, ycc,"o",color="green",label="Datos")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.legend() 
    plt.show()


#Ejecuciones
grafico_a_lineal()
grafico_a_general()
grafico_b_lineal()
grafico_b_general()

