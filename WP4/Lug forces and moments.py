from math import sqrt, atan, pi
import numpy as np

#input forces
F_z = 3106.75 #[N] in direction of flight (axial)
F_y = 1035.58 #[N] in lateral direction (assumed out of s/c)

#RTG input parameters
m_rtg = 52.8 #[kg]
l_rtg = 1.08 #[m] length of rtg
d_rtg = 0.47 #[m] diameter of rtg


#calculating couple moment force on lugs from rtg moment
M_x = F_z * (l_rtg / 2)
dist_lugs = d_rtg #assuming the distance between the lugs is equal to rtg diameter
F_1 = M_x / (dist_lugs)

#top lug net force
F1_ztot = F_z/2
F1_ytot = F_y/2 + F_1
P1 = sqrt(F1_ztot**2 + F1_ytot**2)
theta1 = atan(F1_ytot/F1_ztot) * 360 / (2*pi) #wrt positive z-axis in yz-plane
print(F1_ytot, F1_ztot, P1, theta1)

#bottom lug net force
F2_ztot = F_z/2
F2_ytot = F_y/2 - F_1
P2 = sqrt(F2_ztot**2 + F2_ytot**2)
theta2 = atan(F2_ytot/F2_ztot) * 360 / (2*pi) #wrt positive z-axis in yz-plane
print(F2_ytot, F2_ztot, P2, theta2)


#D_1, w, t_1 calculation inputs
P_cr = max(P1, P2)

K_t = 3
K_bru = 2
F_tu = 10**6 #depends on material

A_t = P_cr / K_t / F_tu #maybe multiply P_cr with sin(theta)
A_br = P_cr / K_bru / F_tu



x = np.sqrt(9)
print(x)








