from math import pi
# import matplotlib.pyplot as plt
import numpy as np

#input forces
F_z = 3106.75  # [N] in direction of flight (axial)
F_y = 1035.58  # [N] in lateral direction (assumed out of s/c)

# materials: 4130 steel, 8630 steel, 2014-t6, 2024-t4, 2024-t3, 7075-t6
ftus = np.array([540, 620, 483, 469, 483, 572])*(10**6)
fyields = np.array([460, 550, 414, 324, 345, 503])*10**6
rhos = np.array([7850, 7850, 2800, 2780, 2780, 2810])

# possibilities for variables:
widths = np.arange(1, 20, 0.25)*0.001
WDs = np.arange(1.2, 5.01, 0.2)
ts = np.arange(0.005, 0.0001, -0.0005)
f = 0.006  # distance plate-hole


def kty(ratio):
    kt = -0.3359*ratio*ratio + 1.3813*ratio - 0.007
    return kt


for mat in range(len(fyields)):
    for width in widths:
        for WD in WDs:
            for t in ts:
                D = width*(1/WD)

                # transverse loads
                A1 = (width-D)*0.5
                A2 = width*(1-1/WD)*t
                A3 = A2
                A4 = A1
                A_br = D*t
                A_av = 6/(3/A1+1/A2+1/A3+1/A4)
                K_ty = kty(A_av/A_br)
                P_ty = K_ty*A_br*fyields[mat]
                R_tr = F_y/P_ty

                # axial loads
                A_t
