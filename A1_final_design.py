import numpy as np
from math import sqrt

from Fourpointeight_r import pull_through
from Fourpoint_NEIN import pull_fail_check
from forceratio import force_factor
from bearing_check import bearing_force, FailureTestLug, FailureTestWall
from fastener_spacing import D2, fastener_spacing
# from bearing check import bearing_check

Fx =
Fy =
Fz =
h = 
t1 =
t2 =
t3 =
w =
s =
L =
P =
D1 =
n_f =
location =
a_c1 =
a_c2 =
a_b =
t_max =
t_min =
E_b =
A_sm =
D_fo =
D_fi =
E_a1 =
E_a2 =
Ai =
G_yield =



D2 = D2(w, s)
fastener_spacing(D2, w, L)
bearingforce = bearing_force(Fx, Fz, n_f, location, x_avg, z_avg, x_pos, z_pos)
wallbearingtest = FailureTestWall(MaxBearingStress, t3, D_2, a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, F_tot, D_fo, D_fi, E_a2, t2)
lugbearingtest = FailureTestLug(MaxBearingStress, t2, D_2, a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, F_tot, D_fo, D_fi, E_a1, t3)
pull_through(Fx, Fy, Fz, x_pos, z_pos, x_avg, z_avg, n_f, Ai)#insert all the necessary variables
pull_fail_check(D_fo, D_fi, t2, t3, F_yi, G_yield, Ai, n_f)
if not (lugbearingtest[2] or wallbearingtest[2] or pullfailure):
    print(f"The lug has passed all checks, The MS's are:\n"
          f"lug = {}\n"
          f"Lug backplate bearing = {lugbearingtest[1]}\n"
          f"Spacecraft skin bearing = {wallbearingtest[1]}\n"
          f"Lug backplate bearing with added thermal stresses = {lugbearingtest[3]}\n"
          f"Spacecraft skin bearing with added thermal stresses = {wallbearingtest[3]}\n"
          f"Spacecraft wall pull through = {safety_factors_wall}\n"
          f"Spacecraft lug backplate pull through = {safety_factors_wall}")
else:
    print("The lug has failed one or multiple checks, The MS's are:\           "
            f"lug = {}\n"
          f"Lug backplate bearing = {lugbearingtest[1]}\n"
          f"Spacecraft skin bearing = {wallbearingtest[1]}\n"
          f"Lug backplate bearing with added thermal stresses = {lugbearingtest[3]}\n"
          f"Spacecraft skin bearing with added thermal stresses = {wallbearingtest[3]}\n"
          f"Spacecraft wall pull through = {safety_factors_wall}\n"
          f"Spacecraft lug backplate pull through = {safety_factors_wall}")")

