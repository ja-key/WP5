import numpy as np


def pull_fail_check(D_fo, D_fi, t2, t3, F_yi, G_yield, Ai, n_f):
    Stress = []
    stress_t2 = []
    stress_t3 = []
    pullfailure = False
    for i in range(int(n_f)):
        # Area = (((D_fo/2)**2)-((D_fi/2)**2)) * np.pi
        Stress_i = []
        Stress_i.append(F_yi[i] / (t2 * np.pi * D_fi))
        # Stress_i = [t2]
        Stress_i.append(F_yi[i] / (t3 * np.pi * D_fi))
        # Stress_i = [t2, t3]
        Stress.append(Stress_i)

        # Stress = lug1 [t2, t3], lug2 [t2, t3] ..... [ [ , ], [ , ], ]
        # np.append(Stress, f"{F_yi[i]/Area}")


    for i in range(int(n_f)):
        for j in range(2):
            if Stress[i, j] >= G_yield:
                print("FAILURE")
                pullfailure = True
                if j == 0:
                    print("Pull-through Failure in t2")
                else:
                    print("Pull-through Failure in t3")
                print("Stress was larger by:",  f"{Stress[i,j]-G_yield}")
            else:
                print("Please proceed, no failure in pull-through")

    return pullfailure