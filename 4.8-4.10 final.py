#4.8 till 4.10 together
import numpy as np
from math import sqrt

#4.8: pull through/puss through check
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

#4.9: pull through failure continued
def pull_fail_check(D_fo, D_fi, t2, t3, F_yi, G_yield, Ai, n_f):
    Stress = []
    stress_t2 = []
    stress_t3 = []
    for i in range(int(n_f)):
        Stress_i = []
        Stress_i.append(F_yi[i] / (t2 * np.pi * D_fi))
        # Stress_i = [t2]
        Stress_i.append(F_yi[i] / (t3 * np.pi * D_fi))
        # Stress_i = [t2, t3]
        Stress.append(Stress_i)

        # Stress = lug1 [t2, t3], lug2 [t2, t3] ..... [ [ , ], [ , ], ]

    for i in range(int(n_f)):
        for j in range(2):
            if Stress[i, j] >= G_yield:
                print("FAILURE")
                if j == 0:
                    print("Pull-through Failure in t2")
                else:
                    print("Pull-through Failure in t3")
                print("Stress was larger by:",  f"{Stress[i,j]-G_yield}")
            else:
                print("Please proceed, no failure in pull-through")

#4.10: Fastener type
def force_factor(D_fo, D_fi, E_a, E_b, t2, t3):
    d = D_fi
    print("Please define your desired configuration:")
    print("Please give me head:")
    head = input("Hexagon (1) or Cylindrical Head (2) :")
    if "1" or "hex" in head.lower():
        head = 0.5 * d
    else:
        head = 0.4 * d

    print("Please give me an engaged shank")
    shank = input("Nut (1) or threaded (2) :")
    if "1" or "nut" in shank.lower():
        shank = 0.4 * d
    else:
        shank = 0.33*d
    lock = 0.4 * d
    A = np.pi * (d/2)**2
    delta_b = (1/E_b) * ((head/ A) + (shank/A) + (lock/A) + ((t2+t3)/A))

    delta_a1 = (4 * t2) / (E_a * np.pi * (D_fo ** 2 - D_fi ** 2))
    delta_a2 = (4 * t3) / (E_a * np.pi * (D_fo ** 2 - D_fi ** 2))
    t_ratio = t2/(t3+t2)
    F_ratio = float(t_ratio*(delta_a1 / (delta_a1 + delta_b)) + (1-t_ratio)*(delta_a2 / (delta_a2 + delta_b)) )
    print("Sir, thy requested force ration is:", F_ratio)
    return F_ratio



