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
    return x/2

#Solves u_t + ((u^2)/2)_x = 0
def LW_TwoSteps(a,b,T,ht,hx, u0):
    m=int(T/ht)
    n=int((b-a)/hx)
    
    c=ht/(4*hx) #*a_0 but a_0=1
    A1=np.eye(n-1)/2 + np.eye(n-1)*c
    A1+=np.diag(np.ones(n-2), 1)*(0.5-c)
    A2=np.eye(n-1)/2 - np.eye(n-1)*c
    A2+=np.diag(np.ones(n-2), -1)*(0.5+c)
    
    spacial_steps=np.linspace(a,b,2*n +1)
    sp_steps, sp_steps_half=spacial_steps[::2], spacial_steps[1::2]

    temp_steps=np.linspace(0,T,2*m +1)
    t_steps, t_steps_half= temp_steps[::2], temp_steps[1::2]
    
    initial_cond=np.array([u0(i) for i in sp_steps_half[:-1]], dtype=float)

    sol=np.zeros((m,n-1))
    sol[0,:]=initial_cond
    U1=np.zeros(m)
    U2=np.zeros(m)
    for i in range(1,m):
        U1=A1@sol[i-1, :].T
        U2=A2@sol[i-1, :].T
        sol[i,:]=sol[i,:] + (2*c)*(U2-U1)
    return sol, sp_steps_half[:-1], t_steps_half

def grafico(ini_cond):
    sol, spacial_steps, temp_steps=LW_TwoSteps(a=-1,b=1,T=1,ht=0.25*0.1,hx=0.1, u0=ini_cond)
    t,x=np.meshgrid(temp_steps, spacial_steps)
    t,x=t.T,x.T

    fig=plt.figure()
    ax=fig.add_subplot(111,projection='3d')
    surf1=ax.plot_surface(x,t, sol, rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf1, shrink=0.5, aspect=5, label="Aprox Solution")
    ax.set_xlabel('[x]')
    ax.set_ylabel('[t]')
    ax.set_zlabel('µ')
    plt.show()

grafico(u0_1)
grafico(u0_2)
