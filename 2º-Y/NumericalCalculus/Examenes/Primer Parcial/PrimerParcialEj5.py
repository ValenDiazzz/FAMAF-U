from PrimerParcialEj4 import rsteffensen
from PrimerParcialEj1 import serie_seno


raiz_3 = rsteffensen(serie_seno, 3, 1e-5, 100)[0][-1]
raiz_45 = rsteffensen(serie_seno, 4.5, 1e-5, 100)[0][-1]
raiz_6 = rsteffensen(serie_seno, 6, 1e-5, 100)[0][-1]


#A las siguientes variables se le resta 1 porque el primer elemento de las listas se guarda antes del while.

iteraciones_3 =len(rsteffensen(serie_seno, 3, 1e-5, 100)[0]) - 1
iteraciones_45 =len(rsteffensen(serie_seno, 4.5, 1e-5, 100)[0]) - 1
iteraciones_6 =len(rsteffensen(serie_seno, 6, 1e-5, 100)[0]) - 1

print("Con punto inicial x = 3 converge a {} luego de {} iteraciones.".format(raiz_3, iteraciones_3))
print("Con punto inicial x = 6 converge a {} luego de {} iteraciones.".format(raiz_6, iteraciones_6))
print("Con punto inicial x = 4.5 converge a {} luego de {} iteraciones.".format(raiz_45, iteraciones_45))
