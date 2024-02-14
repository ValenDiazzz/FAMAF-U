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

def g1(t):
    return 0

def g2(t):
    return 0

#Crank-Nicolson scheme for 1D PDE
#interval [a,b], final time T, u0,g1,g2 initial condition, f non homogeneous term
def Cranck_Nicolson(a,b,T,hx,ht,f,u0, g1, g2):
    m=int(T/ht)
    n=int((b-a)/hx)
    A=np.eye(n)*(2)
    A+=np.diag(-np.ones(n-1),1)
    A+=np.diag(-np.ones(n-1),-1)
    A*=ht/(2*(hx**2)) #*beta but beta=1
    
    spacial_steps=np.arange(a,b,hx)
    temp_steps=np.arange(0,T,ht)
    initial_cond=np.array([u0(i) for i in spacial_steps], dtype=float)   
    
    def g(t):
        gg=np.zeros(n)
        gg[0], gg[-1]=g1(t)+g1(t+ht), g2(t)+g2(t+ht)
        return gg/(2*(hx**2))

    def F(t,X):
        return ht*0.5*(f(t,X)+f(t+ht,X)) + g(t)
    
    A1=np.eye(n)+A
    A2=np.eye(n)-A
    sol=np.zeros((m+1,n))
    sol[0,:]=initial_cond
    for i in range(1,m):
        sol[i,:]=np.linalg.solve(A1, A2 @ sol[i-1, :] + F(ht*i,spacial_steps))
    return sol, spacial_steps, temp_steps

sol, spacial_steps, temp_steps=Cranck_Nicolson(a=0,b=1,T=1,hx=0.1,ht=0.025*0.1,f=f,u0=u0, g1=g1, g2=g2)
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