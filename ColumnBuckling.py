1''' Euler Column Buckling '''
import numpy as np

#Calculates critical buckling stress

#R is radius in [m]
#L is length in [m]
#E is E-modulus in [GPa]

def ColBuckle(R, L, E):
    sigma_cr = (np.pi * (E * 10**9) * R*R/(2*L*L))/(10**6)
    return sigma_cr

print(ColBuckle(1, 5, 1))
      
