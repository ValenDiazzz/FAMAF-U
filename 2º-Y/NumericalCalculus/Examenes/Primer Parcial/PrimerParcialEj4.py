import math 
from PrimerParcialEj1 import serie_seno


def rsteffensen(fun,x0, err, mit):
    hx = [x0]
    hf = [fun(x0)]    
    
    x = x0
    i = 0
    while abs(fun(x)) >= err  and i < mit :
        x = x - (fun(x)**2 / (fun(x + fun(x)) - fun(x)) )
        hx.append(x)
        hf.append(fun(x))
        i+=1
    return (hx, hf)



