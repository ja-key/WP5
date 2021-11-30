import numpy as np
import ShellBuckling.py
import ColumnBuckling.py
Fz =                   # Force in the vertical direction on the tank [N]
R =                    # Radius in metres of the tank [m]
L =                    # Total length of the tank in metres [m]
E =                    # Young's Modulus of the material [Pa]
v =                    # Material's poisson ratio []
t1 =                   # thickness of the straight part of the tank [m]
p =                    # internal pressure of the tank [N/m] or [Pa]

sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
sigma_cr_col = ColBuckle(R, L, E)

if sigma_cr_shell > sigma_cr_col:
    print("The column buckling is more critical")
    sigma_cr = sigma_cr_col
elif sigma_cr_col > sigma_cr_shell:
    print("The shell buckling is more critical")
    sigma_cr = sigma_cr_shell
else:
    print("wow the stresses are the same, good luck")
    sigma_cr = sigma_cr_shell

Area = 2* np.pi * R * t1
sigma = Fz/Area

if sigma > sigma_cr:
    print("FAILURE")
    print("Stress exceeds the critical buckling stress")
else:
    print("WORKS!")

