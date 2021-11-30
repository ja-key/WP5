import numpy as np
from math import sqrt

def shellBuckle(p, R, L, E, t1, v):
    Q = (p/E) * (R/t1)**2
    lam = np.ceil(sqrt((12/(np.pi**4))*(L**4)*(1/(t1**2 * R**2))* (1-v**2)))
    k = lam + (12/(np.pi**4))*(L**4)*(1/(t1**2 * R**2))*(1-v**2)*lam
    sigma_cr = np.around((1.983 - 0.983*np.exp(-23.14*Q))*k*((np.pi**2 * E)/(12*(1-v**2)))*(t1/L)**2, decimals= 3)
    print(sigma_cr/(10**6), "MPa")
    return(sigma_cr)

shellBuckle(1000000, 2, 2, 2000, 0.002, 0.31)
    # k = lambda + (12/(np.pi**4))*(L**4)*(1/(t1**2 * R**2))* (1-v**2)* (1/lambda)