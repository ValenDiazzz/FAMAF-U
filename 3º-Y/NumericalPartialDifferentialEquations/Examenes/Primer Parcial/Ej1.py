"""
El código se divide en 3 etapas.
La primera es en la que se define la función que corresponde al método que resolverá 
de manera numérica el problema, y la función que describe el sistema de ecuaciones. 
Los siguientes etapas corresponden a cada una a las dos condiciones iniciales
del problema. Para visualizar las diferentes situaciones se provee las ejecuciones al 
final de todo el código con un parametro llamado "ajuste".

Tanto en la condicion inicial a) como b), las soluciones x,y se estabilizan en 0 y 
la solución z tiende a crecer indefinidamente. Para poder visualizar de una forma mas 
clara lo que pasa realmente en una situacion Depredador-Presa en el corto plazo, resulta 
conveniente ajustar los datos a un periodo de tiempo mas pequeño. Para poder observar esto
se agrego el parametro "ajuste".

Con respecto a la interpretación del sistema, si x,y,z son 3 diferentes especies
podemos analizar cada una de las situaciones iniciales. 
Al parecer x,y son presas, y las especie depredadora corresponde a z. 

En la condicion inicial a), debido a que la cantidad de especie z es pequeña a comparación 
de las especies x y, permite que las presas logren reproducirse a una velocidad mayor de lo 
que son devoradas por un cierto periodo de tiempo, y por lo tanto tienen un crecimiento en su 
población. Pero llegada una cierta cantidad de especie z, estas comienzan a devorar a x,y 
a una velocidad mayor de la que se reproducen.

Por otro lado en la condición inicial b), la cantidad de la especie z es mayor que en la situacion a)
y en este caso no deja que las especies x,y tegan una reproduccion a mayor velocidad de la que son 
devoradas en ningun lapso de tiempo.

NOTA: Se utilizan alrededor de 100000 puntos en la solucion numerica,
y por esta razón tarda unos segundos considerables  a la hora de la
ejecución. 
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation


#Runge-Kutta 4th order for SDE
def RK4(fun, t_0, x_0, h, a,b):
    def F1(t, x, h):
        return h*fun(t, x) 
    def F2(t, x, h):
        return h*fun(t + (h/2), x + F1(t, x, h)/2)
    def F3(t, x, h):
        return h*fun(t + (h/2), x + F2(t, x, h)/2)
    def F4(t, x, h):
        return h*fun(t + h, x + F3(t, x, h))
    
    sol=[x_0]
    
    #Discretization
    steps=np.arange(a,b,h,dtype=float) if h>0 else np.arange(b,a,h,dtype=float)
    steps=np.append(steps, b) if h>0 else np.append(steps, a)
    
    #Solutions
    for t in steps[1:]:
        x_0= x_0 + (1/6)*(F1(t, x_0, h) + 2*F2(t, x_0, h) + 2*F3(t, x_0, h) + F4(t, x_0, h))
        sol.append(x_0)
    sol=np.array(sol, dtype=float)
    
    return sol.T, steps

#Función que describe el SDE
def fun(t,x):
    #Tomamos x[0]=x, x[1]=y, x[2]=z
    res=np.zeros(3)
    res[0]= (x[0]*0.35) - (0.6*x[0]*x[2])
    res[1]= (x[1]*0.3) - (0.5*x[1]*x[2])
    res[2]= -(x[2]*0.37) + (0.04*x[0]*x[2]) + (0.035*x[1]*x[2])
    return res

plt.style.use("dark_background")



##################### INCISO a) ###################################
def inciso_a(ajuste:bool):
    sol, steps=RK4(fun, 0, [0.8, 2.4, 0.2], 0.001, 0,100) #Solucion numerica del sistema
    if ajuste:
        t=steps[:20000:30]
        y1, y2, y3=sol[0][:20000:30], sol[1][:20000:30], sol[2][:20000:30]

        #Animación
        fig, ax = plt.subplots(figsize=(16,9))
        line1= ax.plot(t[0],y1[0], label="x")[0]
        line2= ax.plot(t[0],y2[0], label="y")[0]
        line3= ax.plot(t[0],y3[0], label="z")[0]
        ax.set(xlim=[0, 20], ylim=[-0.1, 22], xlabel='Time [years]', ylabel='N° of Animals')
        ax.grid(color="white", linewidth=0.4, alpha=0.3, zorder=0)

        line1.set_color("lime")
        line2.set_color("white")
        line3.set_color("orange")
        plt.suptitle('Graficos ajustados (t,~x) (t,~y) (t,~z)')
        ax.legend()


        def update(frame):
            # for each frame, update the data
            line1.set_xdata(t[:frame])
            line1.set_ydata(y1[:frame])

            line2.set_xdata(t[:frame])
            line2.set_ydata(y2[:frame])

            line3.set_xdata(t[:frame])
            line3.set_ydata(y3[:frame])
            return (line1, line2, line3)


        anim = matplotlib.animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=2, blit=True)
        plt.show()
    else:
        fig, (ax1, ax2, ax3)= plt.subplots(3,1,figsize=(16,9),dpi=100)
        ax1.plot(steps[::100], sol[0][::100],color="lime",label="x")
        ax2.plot(steps[::100], sol[1][::100],color="white",label="y")
        ax3.plot(steps[::100], sol[2][::100],color="orange",label="z")
        ax1.set(ylabel='N° of Animals')
        ax2.set(ylabel='N° of Animals')
        ax3.set(xlabel='Time [years]', ylabel='N° of Animals')
        ax1.legend()
        ax2.legend()
        ax3.legend()
        plt.suptitle('Graficos (t,~x) (t,~y) (t,~z)')
        plt.legend()
        plt.show()



##################### INCISO b) ###################################
def inciso_b(ajuste:bool):
    sol, steps=RK4(fun, 0, [2, 1.4, 1], 0.001, 0,100) #Solucion numerica del sistema
    
    if ajuste:
        t=steps[:60000:58]
        y1, y2, y3=sol[0][:60000:58], sol[1][:60000:58], sol[2][:60000:58]

        #Animación
        fig, ax = plt.subplots(figsize=(16,9))
        line1= ax.plot(t[0],y1[0], label="x")[0]
        line2= ax.plot(t[0],y2[0], label="y")[0]
        line3= ax.plot(t[0],y3[0], label="z")[0]
        ax.set(xlim=[0, 22], ylim=[-0.1, 17], xlabel='Time [years]', ylabel='N° of Animals')
        ax.grid(color="white", linewidth=0.4, alpha=0.3, zorder=0)

        line1.set_color("lime")
        line2.set_color("white")
        line3.set_color("orange")
        plt.suptitle('Graficos ajustados (t,~x) (t,~y) (t,~z)')
        ax.legend()


        def update(frame):
            # for each frame, update the data
            line1.set_xdata(t[:frame])
            line1.set_ydata(y1[:frame])

            line2.set_xdata(t[:frame])
            line2.set_ydata(y2[:frame])

            line3.set_xdata(t[:frame])
            line3.set_ydata(y3[:frame])
            return (line1, line2, line3)


        anim = matplotlib.animation.FuncAnimation(fig=fig, func=update, frames=len(t), interval=2, blit=True)
        plt.show()
    else:
        fig, (ax1, ax2, ax3)= plt.subplots(3,1,figsize=(16,9),dpi=100)
        ax1.plot(steps[::100], sol[0][::100],color="lime",label="x")
        ax2.plot(steps[::100], sol[1][::100],color="white",label="y")
        ax3.plot(steps[::100], sol[2][::100],color="orange",label="z")
        ax1.set(ylabel='N° of Animals')
        ax2.set(ylabel='N° of Animals')
        ax3.set(xlabel='Time [years]', ylabel='N° of Animals')
        ax1.legend()
        ax2.legend()
        ax3.legend()
        plt.suptitle('Graficos (t,~x) (t,~y) (t,~z)')
        plt.legend()
        plt.show()



#################### EJECUTABLES ####################################

inciso_a(ajuste=False)
inciso_a(ajuste=True)
inciso_b(ajuste=False)
inciso_b(ajuste=True)