import numpy as np
from math import sqrt

from 4.8_r import pull_through
from 4_NEIN import pull_fail_check
from 4.10 import force_factor
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
bearing_force()
FailureTestLug()
FailureTestWall()
pull_through() #insert all the necessary variables
pull_fail_check()
force_factor()
