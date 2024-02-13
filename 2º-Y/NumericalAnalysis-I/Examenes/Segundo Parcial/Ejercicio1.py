import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

datos = np.loadtxt("./irma.csv", delimiter =",")

horas = datos[:, 0]
longitud = datos[:, 1]
latitud = datos[:, 2]

def graficar_puntos():
    fig, ax= plt.subplots()
    plt.plot(longitud, latitud,"o",color="yellow",label="Data")
    ax.set_xlabel("Longitud")
    ax.set_ylabel("Latitud")
    ax.legend() 
    plt.show()

def ilagrange(abscisa, imagen, x_list):
    px = []
    for x in x_list:
        sumatoria = 0
        j = 0
        for xi in abscisa:
            productoria = 1
            
            for xj in abscisa:
                if xj != xi:
                    productoria = productoria * ((x - xj)/(xi-xj))
            
            sumatoria = productoria*imagen[j] + sumatoria
            j+=1

        px.append(sumatoria)

    return px


def graficar_longitud():
    hrs_dia = [x for x in range(25)]    

    f2 = interpolate.interp1d(horas, longitud, kind="cubic", fill_value="extrapolate")

    fig, ax= plt.subplots()
    plt.plot(hrs_dia, f2(hrs_dia),"o",color="blue",label="SplineCubico")
    plt.plot(hrs_dia, ilagrange(horas, longitud, hrs_dia),"o",color="green",label="Lagrange")
    plt.plot(horas, longitud,"o",color="yellow",label="Data")
    ax.set_xlabel("Horas")
    ax.set_ylabel("Longitud")
    ax.legend() 
    plt.show()



def graficar_latitud():
    hrs_dia = [x for x in range(25)]

    f1 = interpolate.interp1d(horas, latitud, kind="cubic", fill_value="extrapolate")#spline cubico

    fig, ax= plt.subplots()    
    plt.plot(hrs_dia, f1(hrs_dia),"o", color="black",label="SplineCubico")
    plt.plot(hrs_dia, ilagrange(horas, latitud, hrs_dia),"o",color="green",label="Lagrange")
    plt.plot(horas, latitud,"o",color="yellow",label="Data")
    ax.set_xlabel("Horas")
    ax.set_ylabel("Latitud")
    ax.legend() 
    plt.show()


#Ejecuciones
graficar_puntos()
graficar_latitud()
graficar_longitud()