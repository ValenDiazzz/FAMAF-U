import math

#x = valor  

def serie_seno(x):
    suma = 0   #En esta variable se iran almacenando las sumas

    for n in range(5):    
        suma = (((-1)**n) / math.factorial((2*n) + 1)) * (x**((2*n) + 1)) + suma
    
    return suma

#print(serie_seno(x))


