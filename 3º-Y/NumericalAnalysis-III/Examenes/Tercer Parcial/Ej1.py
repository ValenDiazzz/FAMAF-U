import numpy as np
import scipy as sc
import matplotlib.pyplot as plt


#This function solves -u"=f, a<x<b, u(a)=u(b)=0
#using finite elements theory. With phi(x) linear
def finelem(f,grid):
    def phi(x,i,h,grid): #span(phi)=V
        if grid[i-1]<=x<=grid[i]:
            return (x-grid[i-1])/h
        elif grid[i]<=x<=grid[i+1]:
            return (grid[i+1]-x)/h
        else:
            return 0

    def fun(x,i,h,grid): #integrand that defines F_i
        return f(x)*phi(x,i,h,grid)
    h=grid[1]-grid[0]
    n=grid.shape[0]-2
    sol=np.zeros(n+2)
    A=np.eye(n)*2
    A-=np.diag(np.ones(n-1),1)
    A-=np.diag(np.ones(n-1),-1)
    A/=h
    F=np.array([sc.integrate.quad(fun,grid[i-1],grid[i+1] ,args=(i,h,grid))[0] for i in range(1,n+1)])
    sol[1:-1]=np.linalg.solve(A,F)

    return sol

a,b= 0,1
M=10
grid1=np.array([0, 0.1, 0.3, 0.333, 0.5, 0.75, 1])
grid2=np.linspace(a,b,M)


def f1(x):
    return np.pi**2 * np.sin(np.pi*x)

sol1=finelem(f1,grid1)
sol2=finelem(f1,grid2)

fig, ax=plt.subplots()
ax.plot(grid1, sol1, color="cyan",label="non equidistant grid")
ax.plot(grid2, sol2, color="purple",label="equidistant grid")
ax.plot(np.linspace(a,b,200), np.sin(np.pi*np.linspace(a,b,200)), color="black",label="analitic solution")
plt.suptitle("a)")
plt.legend()
plt.show()