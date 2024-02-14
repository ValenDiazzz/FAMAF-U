import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
from RungeKutta import RK4

#Uso a=0, b=1, g1=0, g2=0
beta=1
def sol_an(t,x):
    return np.cos(t)*np.sin(np.pi*x) * x**2

def u0(x):
    return np.sin(np.pi*x) * x**2

def f(t,x):
    ut=-np.sin(t)*np.sin(np.pi*x)*(x**2)
    uxx=np.cos(t)*((-(np.pi**2)*(x**2)*np.sin(np.pi*x)) + (4*np.pi*x*np.cos(np.pi*x)))
    uxx+=np.cos(t)*2*np.sin(np.pi*x)
    return ut - beta*uxx

def g1(t,x):
    return 0

def g2(t,x):
    return 0

#Method of Lines for 1D PDE
#interval [a,b], final time T, u0,g1,g2 initial condition, f non homogeneous term
def MOL(a,b,T,hx,ht,f,u0, g1, g2):
    n=int((b-a)/hx)
    A=np.eye(n)*(-2)
    A+=np.diag(np.ones(n-1),1)
    A+=np.diag(np.ones(n-1),-1)
    A/=hx**2 #*beta but beta=1
    
    spacial_steps=np.arange(a,b,hx)
    initial_cond=np.array([u0(i) for i in spacial_steps], dtype=float)   
    
    def g(t):
        gg=np.zeros(n)
        gg[0], gg[-1]=g1(t), g2(t)
        return gg

    def F(t,X):
        return np.array(A@X + f(t,spacial_steps))
    
    sol, temp_steps=RK4(F,0,T,initial_cond,ht)
    return sol, spacial_steps, temp_steps

sol, spacial_steps, temp_steps=MOL(a=0,b=1,T=1,hx=0.1,ht=0.025*0.1,f=f,u0=u0, g1=g1, g2=g2)
t,x=np.meshgrid(temp_steps, spacial_steps)
t,x=t.T,x.T



fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
surf1=ax.plot_surface(x,t, sol, rstride=1, cstride=1,cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf2=ax.plot_surface(x,t, sol_an(t,x), rstride=1, cstride=1,cmap=cm.Purples, linewidth=0, antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf1, shrink=0.5, aspect=5, label="Aprox Solution")
fig.colorbar(surf2, shrink=0.5, aspect=5, label="Analitic Solution")
plt.show()