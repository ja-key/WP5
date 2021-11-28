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
pullthroughforce = pull_through() #insert all the necessary variables
if not (FailureTestLug() or FailureTestWall() or pull_fail_check()):
    print(f"The lug has passed all checks, The MS's are:\n"
          f"")
else:
    print("The lug has failed one or multiple checks, the checks failed are:\n"
          "")

FailureTestWall()
pull_fail_check()
force_factor()
