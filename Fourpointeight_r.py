import numpy as np
from math import sqrt

def pull_through(Fx, Fy, Fz, x_pos, z_pos, x_avg, z_avg, n_f, Ai):
    denom = []
    for i in x_pos:
        for j in z_pos:
            denom.append(((i-x_avg)**2 + (j-z_avg)**2) * Ai)
    denominator = np.sum(denom)
    r = []
    F_yi = []
    M_cgz = []
    for i in x_pos:
        for j in z_pos:
            r_i = sqrt((i - x_avg) ** 2 + (j - z_avg) ** 2)
            r.append(r_i)
            M_cgz_i = Fx * (j - z_avg) + Fz * (i - x_avg)
            M_cgz.append(M_cgz_i)
            F_pi = Fy/n_f
            F_pmz = (M_cgz_i * Ai * r_i) / (denominator)
            F_yi.append(F_pi + F_pmz)
    return F_yi
