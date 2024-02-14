
import math
import matplotlib.pyplot as plt
import numpy as np

#Ej 1
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
    return hx, hf

#Ej 2
#a)
def fun_lab2ej2a(x):
    return (2*x) - math.tan(x)

hx1, hy1 = rbisec(fun_lab2ej2a, [-4, 4], 1e-15, 1000) 
#print(f"Aproximación:{hx1[-1]}\nCantidad de iteraciones necesarias:{len(hx1)}" )

#b)
def fun_lab2ej2b(x):
    return (x**2) - 3

hx2, hy2 = rbisec(fun_lab2ej2b, [-4, 4], 1e-15, 1000) 
#print("Aproximacion: ", hx2[-1])

#c)

fig, ax = plt.subplots()
x=np.linspace(-4, 4, 200)

ax.plot(hx1, hy1,'*', label="2a")
ax.plot(x,(2*x) - np.tan(x),'-.', label="original(a)" )
ax.plot(hx2, hy2, '*', label="2b")
ax.plot(x, (x**2) - 3, label="original(b)")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("EJERCICIO 2 c)")
plt.legend()
plt.show()

#Ej 3
def fun1(x):
    return x**3 - 1

def fun_derivada(x):
    return 3*(x**2)

def imagenes(x0):
    return[fun1(x0), fun_derivada(x0)]

def rnewton(fun,x0, err, mit):
    hx = []
    hf = []    
    
    x = x0
    i = 0
    error_relativo = 1
    while abs(fun(x)[0]) >= err  and i <= mit and error_relativo>=err :
        
        hx.append(x)
        hf.append(fun(x)[1])
        x = x - (fun(x)[0]/fun(x)[1])   #Cambio: en el primer termino tenía hx[i], pero lo reemplazé por x
        error_relativo = abs((x- hx[-1]) / x)
        i+=1
    
    if len(hx) == 0 and len(hf)==0:
        hx.append(x)
        hf.append(fun(x)[1])
    return hx, hf

#print(rnewton(imagenes, 16, 10e-8, 30))

#Ej4


def raiz_cubica(a):
    def cubica(x, a):
        return x**3 - a
    def cubica_derivada(x):
        return 3*(x**2)
    def imagenes2(x0):
        return [cubica(x0, a), cubica_derivada(x0)]
    
    x0 = 2*a  #propongo un x0 > a porq creo q usa menos pasos
    hx=rnewton(imagenes2, x0, 10e-7, 50 )[0]
    
    return hx[-1]

#print(raiz_cubica(729)) #9

#Ej 5
def fun(x):
    return 2**(x-1)

def ripf(fun, x0, err, mit):
    
    hx = []
    x = x0
    err_absoluto = 1
    
    j=0
    while j < mit and err_absoluto >=err:
        hx.append(x)
        x =fun(hx[j])
        err_absoluto = abs(x - hx[j])
        j+=1
    return hx

#print(ripf(fun, 1.5, 10e-10, 50))

#Ej 6
def fun_lab2ej6(x):
    return 2**(x-1)

hx = ripf(fun_lab2ej6, 2, 10e-5, 100)
#print(hx[-1])           #desde (-inf, 2) me asegura q converge, cuando x0>2+err me da overflow

#Ej 7
def lab2ej7bisec(x):
    def ec(y):
        return y - math.exp(-((1-x*y)**2))
    y = rbisec(ec, [0, 1.5], 1e-5, 200)[0][-1]
    return y
print(lab2ej7bisec(0.7))

def lab2ej7newton(x):
    def ec(y):
        return y - math.exp(-((1-x*y)**2))
    def ec_derivada(y):
        return 1 - 2*math.exp(-(1-x*y)**2)*(x-(x**2)*y)    
    def imagen_ec(y):
        return [ec(y), ec_derivada(y)]
    
    y0 = 1   #con y0>=0.9 me anda
    hy, _= rnewton(imagen_ec, y0, 10e-5, 100)
    return hy[-1]
print(lab2ej7newton(0.7))

def lab2ej7ripf(x):
    # funcion de la que buscar una raiz
    def ec(y): 
        return math.exp(-((1-x*y)**2))

    # Al despejar la ecuacion y = e**(-(1-xy)**2),
    # Obtenemos ln y = -((1-xy)**2), osea que ln y<0
    # Por lo tanto y esta entre 0 y 1.
    # Uso entonces y0 = 0.5

    y0 = 0.5
    hy = ripf(ec, y0, 1e-5, 200)
    return hy[-1]

print(lab2ej7ripf(0.7))







#Ej 8
def deriv1ra_ej8(x):
    return (   ( (x/(math.cos(x))**2))-(2*math.tan(x))) / (x**3)

def deriv2da_ej8(x):
    return 2*(x**2*(1/math.cos(x))**2 * math.tan(x)-2*x*(1/math.cos(x))**2+3*math.tan(x))/x**4


def imagenes3(x):
    return[deriv1ra_ej8(x), deriv2da_ej8(x)]
minimo = rnewton(imagenes3, 1.5, 10e-12, 100)[0][-1] #[0] para seleccionar la lista hx, [-1] para seleccionar el ultimo elemento de hx
imagen_minimo = math.tan(minimo)/(minimo**2)
print("El minimo es en: ({}, {})".format(minimo, imagen_minimo)) #nota: es re preciso


#Ej 9
#0 = 0.01328 D^2 V^3 - E
def molino(x):
    v=24
    e=500
    return 0.01328*(x**2)*(v**3) - e

def molino_derivada(x):
    v=24
    e=500
    return 0.01328*(2*x)*(v**3) - e

def imagenes(x):
    return[molino(x), molino_derivada(x)]

d = rnewton(imagenes, 16, 10e-8, 30)[0][-1]
print(d)    


