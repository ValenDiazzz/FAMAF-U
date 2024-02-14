import numpy as np

from scipy.integrate import quad

def f(x):
    return x*np.exp(-(x**2))
def S(f, a, b):
    return (b-a)/6 * (f(a) + 4*f((a+b)/2) + f(b))


error = 100

def integral(a, b, tol):  
    c = (a+b)/2

    q = S(f, a, b)
    q1 = S(f, a, c)
    q2 = S(f, c, b)

    error = q-q1-q2
    
    if error >= tol:
        q1 = integral(a, c, tol/2)
        q2 = integral(c, b, tol/2)

    return q1 + q2

print(integral(0, 1, 1e-100))






