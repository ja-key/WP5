from math import sqrt, atan, pi
import numpy as np

#Launch Conditions
L = 1035.58
A = 3106.75

#RTG input parameters
m_rtg = 52.8 #[kg]
l_rtg = 1.08 #[m] length of rtg
d_rtg = 0.47 #[m] diameter of rtg
d_fin = 0.1  #[m] spacing left for fins
d_beams = 0.98 #[m]
alpha_in = pi/3 #[rad]

#Coefficients of F1 and F2
coeff = np.array([[np.sin(alpha_in), np.sin(alpha_in)],
                  [np.cos(alpha_in), -np.cos(alpha_in)]])

sol = np.array([[L], [A]])

#finding forces
forces = np.linalg.solve(coeff, sol)
print(forces)
F1 = forces[0]
F2 = forces[1]

#Tension is limiting

F1_y = F1 * np.sin(pi/3)
F1_z = F1 * np.cos(pi/3)

print(F1_y, F1_z)

###top lug net force
##F1_ztot = F_z/2
##F1_ytot = F_y/2 + F_1
##P1 = sqrt(F1_ztot**2 + F1_ytot**2)
##theta1 = atan(F1_ytot/F1_ztot) * 360 / (2*pi) #wrt positive z-axis in yz-plane
##print(F1_ytot, F1_ztot, P1, theta1)
##
###bottom lug net force
##F2_ztot = F_z/2
##F2_ytot = F_y/2 - F_1
##P2 = sqrt(F2_ztot**2 + F2_ytot**2)
##theta2 = atan(F2_ytot/F2_ztot) * 360 / (2*pi) #wrt positive z-axis in yz-plane
##print(F2_ytot, F2_ztot, P2, theta2)


#D_1, w, t_1 calculation inputs
P_cr = max(P1, P2)

K_t = 3
K_bru = 2
F_tu = 10**6 #depends on material

A_t = P_cr / K_t / F_tu #maybe multiply P_cr with sin(theta)
A_br = P_cr / K_bru / F_tu



x = np.sqrt(9)
print(x)








