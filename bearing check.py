import numpy as np
from math import sqrt
def bearing_check(Fx, Fz, n_f, location, x_avg, z_avg, x_pos, z_pos): #Fx is the applied force in the x direction, Fz is the applied force in the z direction, location is the location of the applied force with respect to the coordinate system input is an list of the form [x, z]
    F_ipx = Fx/n_f      #Force applied on the fasteners positive upward
    F_ipz = Fz/n_f      #Force applied on the fasteners positive upward
    M_cgz = Fz*(location[0]-x_avg) + Fx * -(location[1]-z_avg)      #total applied moment on the fasteners with counterclockwise positive
    x_pos = x_pos - x_avg       #changing the origin to the cg of the fasteners
    z_pos = z_pos - z_avg       #changing the origin to the cg of the fasteners
    r_lst = []        #list of positions in radial coordinates from the cg of the fasteners
    F_lst = []      #list of x and z components of the forces on each of the fasteners
    F_tot = []      #list of the total applied force on each fastener
    rot = np.array([0, -1], [1, 0])     #counter clockwise rotational matrix
    for i in x_pos:
        for j in z_pos:                 #iteration through all stringer positions
            r = sqrt(i^2 + j^2)
            u = np.array(i/r, j/r)
            r_lst.append([r, u])        #conversion into radial coordinates
    r_lst = np.array(r_lst)
    SUM = np.sum(np.square(r_lst))      #denominator part of eq 4.4 from the reader
    for i in r_lst:
        F_ipm = (M_cgz*i[0])/SUM
        F = np.multiply(np.matmul(rot, i[1]), F_ipm)
        F_lst.append((F_ipx + F[0], F_ipz + F[1])) #addition of the components
    for i in F_lst:
        F_tot.append(sqrt(i[0]^2 + i[1]^2))

    return (r_lst, F_lst, F_tot)


