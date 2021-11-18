from math import pi, sqrt, sin, cos, tan
import matplotlib.pyplot as plt
import numpy as np

#input forces
F_z = 3106.75  # [N] in direction of flight (axial)
F_y = 1035.58  # [N] in lateral direction (assumed out of s/c)


def curve1(WD):
    Kt = -0.0119*WD*WD+0.0192*WD+0.9846
    return Kt


def curve2(WD):
    Kt = -0.0089*WD*WD*WD+0.051*WD*WD-0.1275*WD+1.0893
    return Kt


def curve3(WD):
    Kt = -0.065*WD+1.0689
    return Kt


def curve4(WD):
    Kt = 0.0107*WD*WD-0.1444*WD+1.141
    return Kt


def curve5(WD):
    Kt = 0.0109*WD*WD-0.1819*WD+1.1652
    return Kt


def curve6(WD):
    Kt = 0.0194*WD*WD-0.3364*WD+1.3196
    return Kt


def curve7(WD):
    Kt = -0.083*WD+0.7534
    return Kt


def get_mass(w, d, t, rho):
    f = 0.006  # distance plate-hole
    flange_mass = ((f+d/2)*w+0.5*pi*w*w*0.25-pi*d*d*0.25) * rho  # rectangle + half circle - hole
    return flange_mass


# possibilities for variables:
widths = np.arange(1, 20, 0.1)*0.001
WDs = np.arange(1.1, 5.01, 0.01)
ts = np.arange(0.0005, 0.005, 0.0001)

# materials: 2014-t6,2024-t4, 2024-t3, 7075-t6
ftus = np.array([483, 469, 483, 572])*(10**6)
rhos = np.array([2800, 2780, 2780, 2810])

Pmax = F_y

for i in range(len(materials)):  # iterate materials
    for width in widths:
        for WD in WDs:
            for t in ts:
                if i == 0:
                    P_u = ftus[i]*(width*(1-1/WD)*t)*curve1
                    mass = get_mass(width, width/WD, t, rhos[i])
                elif i == 1:
