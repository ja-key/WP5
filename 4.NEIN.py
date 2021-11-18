import numpy as np
from math import sqrt

def pull_fail_check(D_fo, D_fi, t2, t3, F_yi, G_yield, Ai, n_f):
    for i in range(n_f):
        Area = (((D_fo/2)**2)-((D_fi/2)**2)) * np.pi
        Stress=[]
        np.append(Stress, f"{F_yi[i]/Area}")
    for i in range(n_f):
        if Stress[i] >= G_yield:
            print("FAILURE")
            print("Pull-through Failure")
            print("Stress was larger by:",  f"{Stress[i]-G_yield}")
        else:
            print("Please proceed, no failure in pull-through")

