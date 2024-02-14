import numpy as np
from Ejercicio1 import intenumcomp
import matplotlib.pyplot as plt

def f1(x):
    return np.cos(x)

def senint(xn):
    yn = []
    for x in xn:
        n = int(np.ceil(10*x))     #b-a/n<=0.1  ---> xi/n<=0.1 ---> xi*10<n. Dado que n es entero hay q redondearlo para arriba
        yn.append(intenumcomp(f1, 0, x, n, "trapecio"))
    return yn   

def grafico():
    fig, ax= plt.subplots()
    xn = np.arange(0, 2*np.pi, 0.5)
    yn =senint(xn)
    xx=np.linspace(0, 2*np.pi, 400)
    plt.plot(xn, yn ,color="black", label="aprox")
    plt.plot(xx, np.sin(xx) ,color="green", label="sin")

    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")

    ax.legend()
    plt.show()


grafico()