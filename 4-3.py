from math import pi
# import matplotlib.pyplot as plt
import numpy as np


def curve06(eD):
    kbr = -0.0507*eD**4 + 0.5353*eD**3 - 2.0619*eD**2 + 3.4741*eD - 1.2321
    return kbr


def curve08(eD):
    kbr = -0.0583*eD**4 + 0.6169*eD**3 - 2.3885*eD**2 + 4.0549*eD - 1.4803
    return kbr


def curve10(eD):
    kbr = -0.0585*eD**4 + 0.6268*eD**3 - 2.4618*eD**2 + 4.2581*eD - 1.5711
    return kbr


def curve12(eD):
    kbr = -0.0583*eD**4 + 0.6258*eD**3 - 2.4758*eD**2 + 4.3467*eD - 1.6309
    return kbr


def curve15(eD):
    kbr = -0.0505*eD**4 + 0.5666*eD**3 - 2.3461*eD**2 + 4.316*eD - 1.6518
    return kbr


def curve20(eD):
    kbr = -0.0424*eD**4 + 0.4924*eD**3 - 2.1389*eD**2 + 4.1693*eD - 1.6269
    return kbr


def curve30(eD):
    kbr = -0.0249*eD**4 + 0.3283*eD**3 - 1.6247*eD**2 + 3.6111*eD - 1.4363
    return kbr


def curve40(eD):
    kbr = -0.0239*eD**4 + 0.3203*eD**3 - 1.6129*eD**2 + 3.6533*eD - 1.4698
    return kbr


def curve60(eD):
    kbr = -0.0177*eD**4 + 0.259*eD**3 - 1.4049*eD**2 + 3.401*eD - 1.3866
    return kbr


#input forces
F_z = 1852.32  # [N] in direction of flight (axial)
F_y = 3208.31  # [N] in lateral direction (assumed out of s/c)

# materials: 4130 steel, 8630 steel, 2014-t6, 2024-t4, 2024-t3, 7075-t6
ftus = np.array([540, 620, 483, 469, 483, 572])*(10**6)
fyields = np.array([460, 550, 414, 324, 345, 503])*10**6
rhos = np.array([7850, 7850, 2800, 2780, 2780, 2810])

# possibilities for variables:
widths = np.arange(1, 20, 0.25)*0.001
WDs = np.arange(1.2, 5.01, 0.2)
#ts = np.arange(0.005, 0.0001, -0.0005)
f = 0.006  # distance plate-hole
tDs = np.array([0.06, 0.08, 0.1, 0.12, 0.15, 0.2, 0.3, 0.4, 0.6])
#Stress factor for Shear out bearing


def kty(ratio):
    kt = -0.3359*ratio*ratio + 1.3813*ratio - 0.007
    return kt


luglist = []
for mat in range(len(fyields)):
    for width in widths:
        for WD in WDs:
            for i in range(0, 9):
                #Geometry
                D = width*(1/WD)
                eD = WD
                curves = [curve06(eD), curve08(eD), curve10(eD),
                          curve12(eD), curve15(eD), curve20(eD),
                          curve30(eD), curve40(eD), curve60(eD)]
                t = D*tDs[i]
                A1 = ((width-D)/2 + D/2*(1-np.cos(pi/4)))*t
                A2 = (width-D)*t/2
                A3 = A2
                A4 = A1
                A_br = D*t

                # axial loads
                K_bry = curves[i]
                P_bry = K_bry*A_br*fyields[mat]
                R_a = (F_z/8)/P_bry

                # transverse loads
                A_av = 6/(3/A1+1/A2+1/A3+1/A4)
                K_ty = kty(A_av/A_br)
                P_ty = K_ty*A_br*fyields[mat]
                R_tr = (F_y/8)/P_ty

                # Margin of Safety
                if R_a < 1 and R_tr < 1:
                    MS = 1/((R_a ** 1.6 + R_tr ** 1.6) ** 0.625) - 1
                    if np.logical_not(np.isnan(MS)):  # checks is MS is real
                        print(MS)
                        row = [width, t, D, P_bry, P_ty, MS]
                        luglist.append(row)

lugarr = np.array(luglist)
# array of all the MSs
MSarr = lugarr[:, -1]
MS_min = np.min(MSarr[MSarr > 0])
index_MS_min = np.where(MSarr == MS_min)[0]

print("minimum MS is: ",  np.min(
    MSarr[MSarr > 0]), "with index: ", int(index_MS_min))

print("this makes the best lug have the parameters: ", lugarr[index_MS_min][0])
