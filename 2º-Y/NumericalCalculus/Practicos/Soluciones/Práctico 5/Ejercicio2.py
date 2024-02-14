
import numpy as np
from Ejercicio1 import intenumcomp
#El maximo de e^-x es en x=0 y su valor es f=1. f"(x) = f""(x) = e^-x <= 1 para todo x e [a, b]
def ejecutar():
    def f(x):
        return np.exp(-x)

    a, b=[0, 1]

    metodo = ["pm", "trapecio", "simpson"]
    n = [4, 10, 20]
    for i in range(3):
        aprox_pm = intenumcomp(f, 0, 1, n[i], "pm")
        aprox_tr = intenumcomp(f, 0, 1, n[i], "trapecio")
        aprox_si = intenumcomp(f, 0, 1, n[i], "simpson")
        error_pm = ((b-a)**3) / (6*(n[i]+2))
        error_tr = ((b-a)**3) / (12*n[i])
        error_si = ((b-a)**5) / (180*n[i])

        print("La aproximación con {} intervalos del metodo de punto medio es: {}, su error absoluto es: {}".format(n[i],aprox_pm,error_pm, abs(error_pm-aprox_pm) ))
        print("La aproximación con {} intervalos del metodo de trapecio es: {}, su error absoluto es: {}".format(n[i], aprox_tr, error_tr,abs(error_tr-aprox_tr) ))
        print("La aproximación con {} intervalos del metodo de simpson es: {}, su error absoluto es: {}".format(n[i],aprox_si, error_si, abs(error_si-aprox_si) ))
        print("\n")
ejecutar()