import numpy as np
from math import sqrt

def pull_through(Fx, Fy, Fz, x_pos, z_pos, x_avg, z_avg, n_f, Ai):


    for i in range(n_f):
        denom = []
        denom.append(((x_pos[i]-x_avg)**2 + (z_pos[i]-z_avg)**2) * Ai)
    denominator = np.sum(denom)


    for i in range(n_f):
        r = []
        r_i = sqrt((x_pos[i] - x_avg) ** 2 + (z_pos[i] - z_avg) ** 2)
        r.append(r_i)
        M_cgz = []
        M_cgz_i = Fx * (z_pos[i] - z_avg) + Fz * (x_pos[i] - x_avg)
        M_cgz.append(M_cgz_i)
        F_pi = Fy/n_f
        F_pmz = (M_cgz[i] * Ai * r_i) / (denominator)
        F_yi = []
        F_yi.append(F_pi + F_pmz)
    return(F_yi)
