import math
import random


#Ej1

def diferentes(x, y, z):
    print("x/y + z =",x/y + z)
    print("x/(y + z) =",x/(y + z))
    print("x/y*z =", x/y*z)
    print("x/(y*z) =", x/(y*z))
diferentes(1, 2, 3)

#Ej2

a = 1 + 2**-53
b = a**-1
print(b)

c = 1 + 2**-52
d = c**-1
print(d)
#Básicamente que el número mas pequeño que la máquina interpreta...
#...que es diferente de cero al sumárseña a 1. Este número es 2^-52 ~ 2,2204.10^-16   


#Ej3

def overfl(n):
    potencia = 1
    n = 1
    while math.isinf(potencia) == False:
        potencia = 2.0**n
        n+=1
        print(potencia)
        print("Exponente:", n)
overfl(2000)


def underfl(n):
    potencia = 1
    n = 1
    while potencia != 0:
        potencia = 2.0**-n
        n+=1
        print(potencia)
    return n

print(underfl(54))


#Ej4 
def sumadecimal(n):
    x = 0
    while x != 10:
        x = x + n
        print(x)

sumadecimal(0.1) #Nunca es 10 exacto dado que 0.1 no tiene representacion finita en sistema de numeración binario
sumadecimal(0.5)


#Ej 5
def factorial1(n):

    if n==0:
        return 1
    else:
        resultado = 1
        for i in range(1, n+1):
            resultado = resultado*i
        return resultado

print(factorial1(6))

#Existe la funcion factorial(x) en la libreria math


#Ej 6
def mayor_forma1(n ,m):
    if n > m:
        print("el número mayor es {}".format(n))
    elif n == m:
        print("Los números son iguales")
    else:
        print("el número mayor es {}".format(m))

def mayor_forma2(n, m):
    
    numeros = [n, m]
    if numeros[0] == numeros[1]:
        print("Lós números son iguales, el max es:{}".format(numeros[0]))
    else:
        mayor = max(numeros)
        print("El número mayor es: {}".format(mayor))

mayor_forma1(2, 2)



#Ej 7

def potencias(x, n):
    for i in range(1, n):
        print("{}^{} = {}".format(x, i, x**i))
    print("{}^{} = {}".format(x, n, x**n))

potencias(2, 7)

#Ej 8

def baskara(a, b, c):  #Este método es el "MALO"    
    discriminante = b**2 - (4*a*c)
    if discriminante < 1:
        raiz1 = "(-{} + ({})**0.5)/ 2{}".format(b, discriminante, a)
        raiz2 = "(-{} - ({})**0.5)/ 2{}".format(b, discriminante, a)
    else:
        raiz1 = (-b + math.sqrt(discriminante) )/2*a
        raiz2 = (-b - math.sqrt(discriminante) )/2*a
    return raiz1, raiz2


def raices(a, b, c):
    discriminante = b**2 - (4*a*c)
    
    if discriminante < 1:
        raiz1 = "(-{} + ({})**0.5)/ 2{}".format(b, discriminante, a)
        raiz2 = "(-{} - ({})**0.5)/ 2{}".format(b, discriminante, a)
    else: #El método mas eficiente usa a raiz1 como el mayor numero en valor absoluto 
        if b >0:
            raiz1 = (-b - math.sqrt(b**2 - (4*a*c)) )/2*a
            raiz2 = c/(a*raiz1)
        else:
            raiz1 = (-b + math.sqrt(b**2 - (4*a*c)) )/2*a
            raiz2 = c/(a*raiz1)
    return raiz1, raiz2

print(baskara(1, 8, 1))
print(raices(1, 8, 1))


#Ej 9 

def horn(coef, x):
    coeficientes = coef + []
    grado = len(coeficientes)-1
    resultado = coeficientes[grado]

    for i in range(grado, 0, -1):
        resultado = resultado * x + coeficientes[i-1]
    return resultado

print(horn([2, -6, 4, 7, -2, 16], 9))


#Ej10

def SonReciprocos(x, y):
    if x*y == 1:
        return True

def numnoreciproc():
    for _ in range(100):

        x = 1 + random.random()
        y = 1/x

        if not SonReciprocos(x,y):
            print(x)
            #print("resultado: {}".format(x*y))
numnoreciproc()
#Conclusión: al hacer 1/x se pierden decimales entonces la multiplicacion no da 1 sino 0.9999999999999999

#Ej 11

def f(x):
    return (((x**2) + 1)**0.5) -1

def g(x):
    return (x**2) / ((((x**2) + 1)**0.5) + 1)

def valuacion_funciones():
    for i in range(20):
        x = 8**-i
        print("f(x)={}, g(x)={}".format(f(x), g(x)))

valuacion_funciones()
#Conclusión:


#Ej 12

def  SonOrtogonales(x1, x2, y1, y2):
    return x1*y1 + x2*y2 == 0


def prueba_ortogonalidad():
    x = [1, 1.1024074512658109]
    y = [-1, 1/x[1]]
    if not SonOrtogonales(x[0], x[1], y[0], y[1]):
        print("Algo salió mal...")

prueba_ortogonalidad()
#Conclusión: Se comete error al calcular con exactitud el recíproco




