import matplotlib.pyplot as plt
import numpy as np
#datos
datos = np.loadtxt("C:/Users/54351/OneDrive/Escritorio/Matemáticas Aplicadas/Análisis Numérico/Datos/datos1a.txt")
x = datos[:, 0]
y = datos[:, 1]


xc = np.linspace(0, 10, 20)
yc= 0.75*xc - 0.5  #Arreglos de numpy se suman coordenadas a coordenadas.
dispersion = np.random.randn(20) #Te devuelve numeros en distribucion normal.
yc_c_dispersion = yc + dispersion #Dispersion normal

#funciones
def cuadrados_minimos_a(x:list, y:list):
    m = len(x)
    sum_y = sum(y)
    sum_x = sum(x)

    sum_x_2 = 0
    sum_x_y = 0 
    for i in range(m):  
      sum_x_2 = x[i]**2 + sum_x_2
      sum_x_y = x[i]*y[i] + sum_x_y

    a0 = ((sum_x_2*sum_y) - (sum_x_y*sum_x)) / ((m*sum_x_2) - (sum_x)**2) #Termino independiente
    a1 = ((m*sum_x_y) - (sum_x*sum_y)) / ((m*sum_x_2) - (sum_x**2)) #Pendiente
    #print("sum_y: {}\nsum_x: {}\nsum_x_2: {}\nsum_x_y: {}".format(sum_y,sum_x, sum_x_2, sum_x_y))
    return a0, a1


def cuadrados_minimos_b(x:list, y:list):
    m = len(x)
    sum_y = np.dot(y, np.ones(m))
    sum_x = np.dot(x, np.ones(m))

    sum_x_2 = np.dot(x, x)
    sum_x_y = np.dot(x, y) 

    a0 = ((sum_x_2*sum_y) - (sum_x_y*sum_x)) / ((m*sum_x_2) - (sum_x)**2) #Termino independiente
    a1 = ((m*sum_x_y) - (sum_x*sum_y)) / ((m*sum_x_2) - (sum_x**2)) #Pendiente
    #print("sum_y: {}\nsum_x: {}\nsum_x_2: {}\nsum_x_y: {}".format(sum_y,sum_x, sum_x_2, sum_x_y))
    return a0, a1


#Gráficos
def grafico_a():
    fig, ax= plt.subplots()

    b, a = cuadrados_minimos_a(x, y)
    #print(b, a)

    x2 = np.linspace(0, 5, 200)

    plt.plot(x2, a*x2 + b,color="black", label="aproximación")
    plt.plot(x, y,"o",color="green", label="Datos")

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    ax.legend()
    plt.show()

def grafico_b():
    fig, ax= plt.subplots()

    b, a = cuadrados_minimos_b(x, y)
    #print(b, a)

    x2 = np.linspace(0, 5, 200)

    plt.plot(x2, a*x2 + b,color="green", label="aproximación")
    plt.plot(x, y,"o",color="black",label="Datos2")

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    ax.legend() 
    plt.show()

def grafico_c():
    fig, ax= plt.subplots()
    x1 = np.linspace(0, 10, 400)
    
    coeficientes = np.polyfit(xc, yc_c_dispersion, 1) #Lista con a0 y a1 de cuadrados minimos lineal.
    fx = np.polyval(coeficientes, x1) #Valua el polinomio de grado 1 en los puntos x1

    plt.plot(x1, fx,color="black", label="aproximación")
    plt.plot(xc, yc_c_dispersion,"o",color="orange",label="Datos con disperción")
    plt.plot(xc, yc,"o",color="green",label="Datos")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    ax.legend() 
    plt.show()

#Ejecuciones
grafico_a()
grafico_b()
grafico_c()