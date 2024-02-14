import numpy as np

def fun(x):
    return x**2


def intenumcomp(fun, a, b, n, regla):
    if regla == "pm":
        h = (b-a)/(n+2)
        x = np.linspace(a, a + (n+2)*h, n+3) #xj = a + (j+1).h, j = -1, ..., n+1
        sumatoria = 0
        for j in range(int((n/2)+1)):       #sumatoria
            sumatoria = sumatoria + fun(x[2*j])
        integral= 2*h*sumatoria
    
    elif regla=="trapecio":
        h = (b-a)/n
        x = np.linspace(a, a + n*h, n+1)  #xj = a+j.h
        sumatoria = fun(a)+ fun(b)
        for j in range(1, n):           #sumatoria
            sumatoria = sumatoria + 2*fun(x[j])
        integral = sumatoria * (h/2)
    
    elif regla=="simpson":
        h = (b-a)/n
        x = np.linspace(a, a+n*h,n+1) #xj = a + j.h
        
        sumatoria = fun(a) + fun(b)
        for j in range(1, int(n/2)+1):
            sumatoria = sumatoria + 4*fun(x[(2*j) - 1])
            if j != int(n/2):
                sumatoria = sumatoria + 2*fun(x[2*j])
        
        integral = sumatoria*(h/3)
    return integral


#print(intenumcomp(fun, -1, 1, 10, "pm"))
#print(intenumcomp(fun, -1, 1, 10, "trapecio"))
#print(intenumcomp(fun, -1, 1, 10, "simpson"))
