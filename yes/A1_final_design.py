import numpy as np
from math import sqrt

from Fourpointeight_r import pull_through
from Fourpoint_NEIN import pull_fail_check
from forceratio import force_factor
from bearing_check import bearing_force, FailureTestLug, FailureTestWall
from fastener_spacing import D2, fastener_spacing
# from bearing check import bearing_check
# material is steel:8630 steel S/C:aa7475-T73   LUG: 7075-t6
Fx =   1640.91298269                        #const
Fy =  2842.14465682                          #const
Fz = 1034.45605656                        #const
t1 = 3.2142857142857144*10**-3              #const
t2 = 0.001
t3 = 0.002
w = 7.5*10**-3                               #const
L = 1.6*w
h = (1/3)*L
s = 2.5
P = 3.1167134469523403*10**-3                  #const
D1 = 5.357142857142857*10**-3                 #const
n_f = 4                                          #const
location = [0.5*L, 0.5*w]                           #const
a_c1 = 21.6*10**-6                                    #var based on mat
a_c2 = 21.6*10**-6                                      #var based on  mat
a_b = 11.2*10**-6                                        #var based on mat
t_max = 273.15                                              #const
t_min = 300                                                 #const
E_b = 187*10**9
D_2 = D2(w,L , s)
D_fi = D_2
D_fo = 1.45 * D_fi
E_a1 = 71.7 * 10**9
E_a2 = 71.7 * 10**9
Ai = np.pi * (D_2**2)/4
A_sm = Ai
G_yield =503*10**6                                             #PA
MaxBearingStress = 469*10**6




f_spacing = fastener_spacing(D_2, w, L)
x_pos = f_spacing[0]
z_pos = f_spacing[1]
x_avg = f_spacing[2]
z_avg = f_spacing[3]

bearingforce = bearing_force(Fx, Fz, n_f, location, x_avg, z_avg, x_pos, z_pos)
F_tot = bearingforce[3]
wallbearingtest = FailureTestWall(MaxBearingStress, t3, D_2, a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, F_tot, D_fo, D_fi, E_a2, t2)
lugbearingtest = FailureTestLug(MaxBearingStress, t2, D_2, a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, F_tot, D_fo, D_fi, E_a1, t3)
F_pullthrough = pull_through(Fx, Fy, Fz, x_pos, z_pos, x_avg, z_avg, n_f, Ai)#insert all the necessary variables
pullfailcheck = pull_fail_check(D_fo, D_fi, t2, t3, F_pullthrough, G_yield, Ai, n_f)
if not (lugbearingtest[2] or wallbearingtest[2] or pullfailcheck[0]):
   print("The lug has passed all checks, The MS's are:\n lug = \nLug backplate bearing = {}\n Spacecraft skin bearing = {}\nLug backplate bearing with added thermal stresses = {}\nSpacecraft skin bearing with added thermal stresses = {}\nSpacecraft wall pull through = {}\nSpacecraft lug backplate pull through = {}".format(lugbearingtest[1], wallbearingtest[1], lugbearingtest[3], wallbearingtest[3], pullfailcheck[2], pullfailcheck[1]))


    #print("The lug has passed all checks, The MS's are:\n"
      #    "lug = {}\n"
       #   "Lug backplate bearing = {lugbearingtest[1]}\n"
       #   "Spacecraft skin bearing = {wallbearingtest[1]}\n"
       #   "Lug backplate bearing with added thermal stresses = {lugbearingtest[3]}\n"
         # "Spacecraft skin bearing with added thermal stresses = {wallbearingtest[3]}\n"
        #  "Spacecraft wall pull through = {safety_factors_wall}\n"
         # "Spacecraft lug backplate pull through = {safety_factors_wall}")
else:
    print("The lug has failed one or multiple checks, The MS's are:\n lug = \nLug backplate bearing = {}\n Spacecraft skin bearing = {}\nLug backplate bearing with added thermal stresses = {}\nSpacecraft skin bearing with added thermal stresses = {}\nSpacecraft wall pull through = {}\nSpacecraft lug backplate pull through = {}".format(lugbearingtest[1], wallbearingtest[1], lugbearingtest[3], wallbearingtest[3], pullfailcheck[2], pullfailcheck[1]))

