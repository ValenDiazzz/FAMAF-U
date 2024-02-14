import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def u0_1(x):
    return (x+1)*np.exp(-x/2)
def u0_2(x):
    return 1 if -0.5<=x<=0.5 else 0
def F(x):
    return (x**2)/2

#Solves u_t + ((u^2)/2)_x = 0
def Richtmyer(a,b,T,ht,hx,u0,F):
    m=int(T/ht)
    n=int((b-a)/hx)
    
    A=np.eye(n)*0.5
    A+=np.diag(np.ones(n-1), 1)*0.5
    
    spacial_steps=np.linspace(a,b,2*n +1)
    sp_steps, sp_steps_half=spacial_steps[::2], spacial_steps[1::2]

    temp_steps=np.linspace(0,T,2*m +1)
    t_steps, t_steps_half= temp_steps[::2], temp_steps[1::2]
    
    initial_cond=np.array([u0(i) for i in sp_steps], dtype=float)[:-1]

    sol=np.zeros((m,n)) 
    sol[0,:]=initial_cond
    c=ht/(2*hx)
    for i in range(1,m):
        b=np.array([F(sol[i-1, j])-F(sol[i-1, (j+1)]) for j in range(n-1) ], dtype=float)
        b=c*np.append(b,0)
        sol[i,:]=A@sol[i-1, :].T + b
    
    return sol, sp_steps_half, t_steps_half

def grafico(ini_cond):
    sol, spacial_steps, temp_steps=Richtmyer(a=-1,b=1,T=1,ht=0.25*0.1,hx=0.1, u0=ini_cond,F=F)
    t,x=np.meshgrid(temp_steps, spacial_steps)
    t,x=t.T,x.T

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    surf1=ax.plot_surface(-x,t, sol, rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf1, shrink=0.5, aspect=5, label="Aprox Solution")
    ax.set_xlabel('[x]')
    ax.set_ylabel('[t]')
    ax.set_zlabel('µ')
    plt.show()

grafico(u0_1)
grafico(u0_2)
