from Ejercicio2 import inewton
import matplotlib.pyplot as plt
import numpy as np

#Puntos de 1/x
x=np.linspace(1, 5, 101)

#Puntos de la aproximación
x2=[1, 2, 3, 4, 5]
y2= [1, 1/2, 1/3, 1/4, 1/5]

y_pol_interpolante = inewton(x2, y2, x)

#Gráficos

fig, ax= plt.subplots() 

plt.plot(x, 1/x, label="1/x") 
plt.plot(x, y_pol_interpolante, label="aproximacion")
plt.plot(x2, y2,"o", label="Puntos de interpolación") # = ax.plot(np.array(x2), 1/np.array(x2), '*', "Puntos de interpolación")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_title("Ejercicio 3")
ax.legend() #Sin este comando no muestra el nombre de los graficos
plt.show()

