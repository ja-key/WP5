import numpy as np
from math import sqrt
from thermal_stress_check import thermal_force

F_tot = []  # list of the total applied force on each fastener
def bearing_force(Fx, Fz, n_f, location, x_avg, z_avg, x_pos, z_pos): #Fx is the applied force in the x direction, Fz is the applied force in the z direction, location is the location of the applied force with respect to the coordinate system input is an list of the form [x, z]
    F_ipx = Fx/n_f      #Force applied on the fasteners positive upward
    F_ipz = Fz/n_f      #Force applied on the fasteners positive upward
    M_cgz = Fz*(location[0]-x_avg) + Fx * -(location[1]-z_avg)      #total applied moment on the fasteners with counterclockwise positive
    x_pos = x_pos - x_avg       #changing the origin to the cg of the fasteners
    z_pos = z_pos - z_avg  #changing the origin to the cg of the fasteners
    pos_lst = []  #list of positions in radial coordinates from the cg of the fasteners
    F_lst = []      #list of x and z components of the forces on each of the fasteners

    r_lst = []
    rot = np.array([[0, -1], [1, 0]])     #counter clockwise rotational matrix
    for i in x_pos:
        for j in z_pos:         #iteration through all stringer positions
            r = sqrt(abs(i**2) + abs(j**2))
            u = np.array([i/r, j/r])
            pos_lst.append([r, u])        #conversion into radial coordinates
    for i in pos_lst:
        r_lst.append(i[0])
    r_lst = np.array(r_lst)
    SUM = np.sum(np.square(r_lst)) #denominator part of eq 4.4 from the reader
    for i in pos_lst:
        F_ipm = (M_cgz*i[0])/SUM
        F = np.multiply(np.matmul(rot, i[1]), F_ipm)
        F_lst.append((F_ipx + F[0], F_ipz + F[1])) #addition of the components
    for i in F_lst:
        F_tot.append(sqrt(i[0]**2 + i[1]**2))

    return r_lst, pos_lst, F_lst, F_tot


test = 3106.75, 1035.58, 4, (0.0075, 0.006), 0.0075, 0.005, [0.003, 0.012], (160, 210, 310, 360)
x_pos = np.array([0.003, 0.012])
z_pos = np.array([0.003, 0.007])
print(bearing_force(1035.58, 3106.75, 4, (0.0075, 0.006), 0.0075, 0.005, x_pos, z_pos))

def FailureTestLug(MaxBearingStress, t, D_2, a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, force_ratio, F_tot):  # Tests each fastener for maximum bearing stress (Lug)
    TFail = []  # Creates a list for each fastener
    thermal_force(a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, force_ratio)
    safety_factor = []
    for i in F_tot:
        BearingStress = (i+max(F_dtpluslug, F_dtminlug)) / (D_2*t)
        safety_factor.append(Maxbearingstress/BearingStress - 1)
        if MaxBearingStress > BearingStress:
            TFail.append(0)  # If fastener is sufficiently strong, a 0 is added to the list
        else:
            TFail.append(1)  # If fastener is not sufficiently strong, a 1 is added to the list
    if 1 in Tfail:
        Print('Bearing Failure at lug plate')
    else:
        Print('Bearing check passed in lug plate')
    return (TFail, safety_factor)

print(FailureTestLug(800, 3, 5))


def FailureTestWall(MaxBearingStress, TSpaceWall, D_2, a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, force_ratio F_tot):  # Tests each fastener for maximum bearing stress (SpaceWall)
    TFailWall = []  # Creates a list for each fastener
    safety_factor = []
    thermal_force(a_c1, a_c2, a_b, t_max, t_min, E_b, A_sm, force_ratio)
    for i in F_tot:
        BearingStress = (i+max(F_dtplusskin, F_dtminskin)) / (D_2 * TSpaceWall)
        safety_factor.append(Maxbearingstress/BearingStress - 1)
        if MaxBearingStress > BearingStress:
            TFailWall.append(0)  # If fastener is sufficiently strong, a 0 is added to the list
        else:
            TFailWall.append(1)  # If fastener is not sufficiently strong, a 1 is added to the list
    if 1 in Tfail:
        Print('Bearing Failure at s/c skin')
    else:
        Print('Bearing check passed in s/c skin')
    return (TFailWall, safety_factor)

print(FailureTestWall(800, 3, 5))