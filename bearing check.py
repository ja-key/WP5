import numpy as np
from math import sqrt

F_tot = []  # list of the total applied force on each fastener
def bearing_check(Fx, Fz, n_f, location, x_avg, z_avg, x_pos, z_pos): #Fx is the applied force in the x direction, Fz is the applied force in the z direction, location is the location of the applied force with respect to the coordinate system input is an list of the form [x, z]
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

    return (r_lst,pos_lst, F_lst, F_tot)


test = 3106.75, 1035.58, 20, (250, 250), 250, 260, (50, 150, 250, 350, 450), (160, 210, 310, 360)
x_pos = np.array([50, 150, 250, 350, 450])
z_pos = np.array([160, 210, 310, 360])
print(bearing_check(1035.58, 3106.75, 20, (250, 250), 250, 260, x_pos, z_pos))

def FailureTest(MaxBearingStress, t, D_2, ):
    TFail = []
    for i in F_tot:
        BearingStress = F_tot[0] / (D_2*t)
        if MaxBearingStress > BearingStress:
            TFail.append(0)
        else:
            TFail.append(1)
    return(TFail)

print(FailureTest(800,3,5))