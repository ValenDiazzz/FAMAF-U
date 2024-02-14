import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def u0_1(x):
    return (x+1)*np.exp(-x/2)
def u0_2(x):
    return 1 if -0.5<=x<=0.5 else 0

#Solves u_t + v.u_x=0 with v>=0
def UpWind(a,b,T,ht,hx,u0,v):
    m=int(T/ht)
    n=int((b-a)/hx)
    
    alpha=ht*v/hx
    A=np.eye(n)*(-alpha)
    A+=np.eye(n)
    A+=np.diag(np.ones(n-1), -1)*alpha
    
    spacial_steps=np.arange(a,b,hx)
    temp_steps=np.arange(0,T,ht)
    initial_cond=np.array([u0(i) for i in spacial_steps], dtype=float)
    
    sol=np.zeros((m+1,n))
    sol[0,:]=initial_cond
    sol[0,0]=0
    for i in range(1,m):
        sol[i,:]=A@sol[i-1, :].T
        sol[i,0]=0
    
    return sol, spacial_steps, temp_steps

def grafico(ini_cond):
    sol, spacial_steps, temp_steps=UpWind(a=-1,b=1,T=1,ht=0.025*0.1,hx=0.1,u0=ini_cond,v=1)

    t,x=np.meshgrid(temp_steps, spacial_steps)
    t,x=t.T,x.T

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    surf1=ax.plot_surface(x,t, sol, rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf1, shrink=0.5, aspect=5, label="Aprox Solution")
    plt.show()

grafico(u0_1)
grafico(u0_2)
