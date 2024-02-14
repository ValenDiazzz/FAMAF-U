import numpy as np

def RK4(fun,t0,T,x_0,h):
    def F1(t, x, h):
        return h*fun(t, x) 
    def F2(t, x, h):
        return h*fun(t + (h/2), x + F1(t, x, h)/2)
    def F3(t, x, h):
        return h*fun(t + (h/2), x + F2(t, x, h)/2)
    def F4(t, x, h):
        return h*fun(t + h, x + F3(t, x, h))
    
    sol=[x_0]
    steps=np.arange(t0,T,h,dtype=float) 
    #steps=np.append(steps, T)
    for t in steps[1:]:
        x_0= x_0 + (1/6)*(F1(t, x_0, h) + 2*F2(t, x_0, h) + 2*F3(t, x_0, h) + F4(t, x_0, h))
        sol.append(x_0)
    sol=np.array(sol, dtype=float)
    return sol, steps