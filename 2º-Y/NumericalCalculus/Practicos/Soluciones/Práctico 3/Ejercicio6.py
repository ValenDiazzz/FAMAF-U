import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from Ejercicio2 import inewton
from Ejercicio1 import ilagrange
#from Ejercicio5 import f


x2= [-3, -2, -1, 0, 1, 2, 3]
y2= [1, 2, 5, 10, 5, 2, 1]

x=np.linspace(-3, 3, 200)

pol_newton = inewton(x2, y2, list(x)) #me devuelve una lista
pol_lagrange = ilagrange(x2, y2, list(x))
f = interpolate.interp1d(x2, y2, kind="cubic", fill_value="extrapolate")

print(len(pol_newton))
fig, ax= plt.subplots()

plt.plot(x, pol_newton, label="Newton")
plt.plot(x, pol_lagrange, label="Lagrange")
plt.plot(x, f(x), label="Spline Cúbico")
ax.legend()
plt.show()
