import math
import matplotlib.pyplot as plt
from PrimerParcialEj1 import serie_seno

def signo(x, y):
    return False if (x > 0 and y > 0) or (x < 0 and y < 0) else True


def rbisec(fun, I, err, mit): 
    a = I[0]
    b = I[1]
    c= (a+b)/2
    hx = [c]
    hf = [fun(hx[0])]
    
    j = 0
    while abs(hf[j]) >= err and j+1 < mit: 
        
        if signo(hf[j], fun(a)):
            b = hx[j]
        elif signo(hf[j], fun(b)):
            a = hx[j]     
        
        c= (a+b)/2
        hf.append(fun(c))
        hx.append(c)       
        j+=1
    return (hx, hf)


hx1 = rbisec(serie_seno, [2, 4], 1e-5, 100)[0][-1] #Primera raiz positiva
hy1 = rbisec(serie_seno, [2, 4], 1e-5, 100)[1][-1] #Imagen de la primera raiz positiva

hx2 = rbisec(serie_seno, [4, 6], 1e-5, 100)[0][-1] #Segunda raiz positiva
hy2 = rbisec(serie_seno, [4, 6], 1e-5, 100)[1][-1] #Imagen de la segunda raiz positiva

print("La primera raiz positiva es:",hx1)
print("La imagen de la primera raiz positiva es:",hy1)
print("La segunda raiz positiva es:",hx2)
print("La imagen de la segunda raiz positiva",hy2)

