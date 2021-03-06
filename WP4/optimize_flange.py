from math import pi
# import matplotlib.pyplot as plt
import numpy as np

#input forces
F_z = 3106.75  # [N] in direction of flight (axial)
F_y = 1035.58  # [N] in lateral direction (assumed out of s/c)


# possibilities for variables:
widths = np.arange(1, 20, 0.25)*0.001
WDs = np.arange(1.2, 5.01, 0.2)
ts = np.arange(0.005, 0.0001, -0.0005)
f = 0.006  # distance plate-hole

# materials: 4130 steel, 8630 steel, 2014-t6, 2024-t4, 2024-t3, 7075-t6
ftus = np.array([540, 620, 483, 469, 483, 572])*(10**6)
fyields = np.array([460, 550, 414, 324, 345, 503])*10**6
rhos = np.array([7850, 7850, 2800, 2780, 2780, 2810])

Pmax = 1.5 * F_y / 4
dlist1 = [100000]
dlist2 = [100000]
dlist4 = [100000]
mlist = [1000.0]
deltaP = 0
bestindex = 0
bestwidth = 0
bestwd = 0
bestt = 0
bestmaterial = 0
bestp = 0


## Curve 1
for i in range(2):
    for t in ts:
        for WD in WDs:
            for width in widths:
                P_u = ftus[i]*(width*(1-1/WD)*t)*curve1(WD)
                mass = get_mass(width, width/WD, t, rhos[i])
                sigma_bending = F_y/4*(f+width/WD*0.5)*6/(width*t*t)
                if P_u - Pmax < 100 and P_u - Pmax > 0:
                    if sigma_bending < ftus[i]:
                        bestindex = len(dlist1)-1
                        bestwidth = width
                        bestwd = WD
                        bestt = t
                        bestmaterial = i
                        bestp = P_u


print("Curve 1:", bestwidth, bestwd, bestt,
      bestmaterial, bestindex, len(dlist1))
deltaP = 0
bestindex = 0
bestwidth = 0
bestwd = 0
bestt = 0
bestmaterial = 0
bestp = 0

## Curve 2
for i in [2, 5]:
    for width in widths:
        for WD in WDs:
            for t in ts:
                P_u = ftus[i]*(width*(1-1/WD)*t)*curve2(WD)
                deltaP = Pmax - P_u
                dlist2.append(deltaP)
                sigma_bending = F_y/8*(f+width/WD*0.5)*6/(width*t*t)
                if len(dlist2[:-1]) > 0 and deltaP >= 0:
                    if deltaP <= min(dlist2[:-1]) and sigma_bending < ftus[i]:
                        bestindex = len(dlist2)-1
                        bestwidth = width
                        bestwd = WD
                        bestt = t
                        bestmaterial = i

print("Curve 2:", bestwidth, bestwd, bestt,
      bestmaterial, bestindex, len(dlist2))

deltaP = 0
bestindex = 0
bestwidth = 0
bestwd = 0
bestt = 0
bestmaterial = 0
bestp = 0

## Curve 4
for i in [3, 4]:
    for width in widths:
        for WD in WDs:
            for t in ts:
                P_u = ftus[i]*(width*(1-1/WD)*t)*curve4(WD)
                deltaP = Pmax - P_u
                dlist4.append(deltaP)
                sigma_bending = F_y/8*(f+width/WD*0.5)*6/(width*t*t)
                if len(dlist4[:-1]) > 0 and deltaP >= 0:
                    if deltaP <= min(dlist4[:-1]) and sigma_bending < 0.9*ftus[i]:
                        print('yes')
                        bestindex = len(dlist4)-1
                        bestwidth = width
                        bestwd = WD
                        bestt = t
                        bestmaterial = i

print("Curve 4:", bestwidth, bestwd, bestt,
      bestmaterial, bestindex, len(dlist4))


'''
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
    flange_mass = ((f+d/2)*w+0.5*pi*w*w*0.25-pi*d*d*0.25) * rho
    # rectangle + half circle - hole
    return flange_mass
'''
'''
for i in range(np.size(ftus)):  # iterate materials
    for width in widths:
        for WD in WDs:
            for t in ts:
                if i == 0 or i == 1:
                    P_u = ftus[i]*(width*(1-1/WD)*t)*curve1(WD)
                    mass = get_mass(width, width/WD, t, rhos[i])
                elif i == 2 or i == 5:
                    P_u = ftus[i]*(width*(1-1/WD)*t)*curve2(WD)
                    mass = get_mass(width, width/WD, t, rhos[i])
                elif i == 3 or i == 4:
                    P_u = ftus[i]*(width*(1-1/WD)*t)*curve4(WD)
                    mass = get_mass(width, width/WD, t, rhos[i])

                deltaP = abs(Pmax - P_u)
                dlist.append(deltaP)
                #print(mass)
                mlist.append(mass)
                if len(dlist[:-1]) > 0 and len(mlist[:-1]) > 0:
                    if deltaP <= min(dlist[:-1]):
                        bestindex = len(dlist)-1
                        bestwidth = width
                        bestwd = WD
                        bestt = t
                        bestmaterial = i
'''
