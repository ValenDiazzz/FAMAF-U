import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

#datos es ahora es una matriz de datos de la siguiente página: https://www.tutiempo.net/clima/ws-873440.html
datos = np.loadtxt("C:/Users/54351/OneDrive/Escritorio/Matemáticas Aplicadas/Análisis Numérico/Datos/datos_aeroCBA.txt")

raw_year_data = datos[:, 0] #guarda todas las filas de la columna 0. Puedo elegir cuales filas haciendo desde:hasta
raw_degrees_data = datos[:, 1]
#Limpio los NaN
nan_positions= ~np.isnan(raw_degrees_data) #lista con valores booleanos. Donde dice false hay NaN
year = raw_year_data[nan_positions] #Elimina todos los elementos en las posiciones de los false, es decir los que tienen datos NaN
degrees = raw_degrees_data[nan_positions] #Este concepto se llama máscaras.

f = interpolate.interp1d(year, degrees, kind="cubic", fill_value="extrapolate") #F es una funcion de R a R. Es un spline cúbico

fig, ax= plt.subplots()

x =np.arange(1957, 2018)
plt.plot(x, f(x), label="interpolante")
plt.plot(year, degrees,"o", label="Datos")

ax.legend()
plt.show()

#Temperaturas medias:
k = 0
for temp_media in degrees:
    print("En {} la temperatura media fue:{}".format(int(year[k]), temp_media))
    k+=1
