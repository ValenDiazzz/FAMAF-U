import numpy as np
from scipy.integrate import quad 
from math import sqrt

def pendulo(length, angle):
    angle = (angle/360)*np.pi
    def f(x):
        return 1/( 1 - ((np.sin(angle/2))**2)*(np.sin(x))**2)**0.5
    return sqrt((16*length)/9.8) * quad(f, 0, np.pi/2)[0]
