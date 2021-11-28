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
D =
D2 = D2(w, s)
fastener_spacing(D2, w, L)
bearingforce = bearing_force()
pull_fail_check()
wallbearingtest = FailureTestWall()
lugbearingtest = FailureTestLug()
pull_through(Fx, Fy, Fz, x_pos, z_pos, x_avg, z_avg, n_f, Ai) #insert all the necessary variables
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

