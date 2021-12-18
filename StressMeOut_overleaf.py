import numpy as np
import pygame as pg
from ShellBuckling import shellBuckle
from ColumnBuckling import ColBuckle

''' Tank dimesions and properties'''

R = 1.50                   # Radius in metres of the tank [m]
L = 5.71                   # Total length of the tank in metres [m]
E = 78 * 10**9             # Young's Modulus of the material [Pa]
v = 0.33                   # Material's poisson ratio []
t1 =  6.43 * 10**(-3)      # thickness of the straight part of the tank [m]
p =  21 * 10**5            # internal pressure of the tank [N/m] or [Pa]
t2 =  3.22 * 10**(-3)      # Thickness of the spherical caps [m]
rho = 2700                 # Density of material used for tank [kg/m^3]
sigma_y = 490e6            # Yield stress of material [Pa]
col_ind = "N"              # Check if tank had failed in column buckling
shell_ind = "N"            # Check if tank had failed in shell buckling
mAttatch = 281.1           #Mass of the attatchments
D0 = 0.104
# Initial
##mAttatch = 0
##D0 = 0.4/2.4

''' Start of procedure '''

#Calculation of critical buckling stresses
sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
sigma_cr_col = ColBuckle(R, L, E)

#Constraint on minimum length of straight section
L_min = 2.4 * D0


#Function to calculate full mass of tank (structure+propellant+attacthments) 
def TankMass(rho, R, L, t1, t2):
    mass = rho*(2*np.pi*R*t1*(L-2*R) + 4*np.pi*R*R*t2) + 39284 + mAttatch
    return mass

#Constant internal volume
V = 33.3    #Volume in [m^3]

#Compressibe forces and stresses
Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
Area = 2* np.pi * R * t1
sigma = (Fz/Area)/(10**6)

#Empty lists to be used
Rs = []
Ls = []
masses = []

''' Euler Column Buckling Check '''

if sigma > sigma_cr_col:
    col_ind = "Y"
    R_cr = L/np.pi * np.sqrt((2*sigma)/E) #Finds critical radius
    if R_cr > 2.2:     #Upper boundary for radius
        R_cr = 2.21
    for Ri in np.arange(R, R_cr, 0.01): #iterate over radii
        Li = 2/3*Ri+V/(np.pi*Ri*Ri)     #Find corresponding lengths
        sigma_col = ColBuckle(Ri, Li, E)
        t1i = p*Ri/(sigma_y)        #Find corresponding thicknesses
        t2i = p*Ri/(2*sigma_y)
        if Li < 2*Ri + L_min:           #Minimum straight section condition
            break

        #Only configurations which pass failure check are taken
        if sigma_col > sigma:
            Rs.append(Ri)
            Ls.append(Li)
            masses.append(TankMass(rho, Ri, Li, t1i, t2i))

    #Inform user that no configuration exists such that conditions are met
    if len(Rs) == 0:
        print("Change material")
        pg.quit()
    massArr = np.array(masses)
    minIndex = np.where(massArr == np.min(massArr))[0]  #Finds index of lightest tank
    R = Rs[minIndex]    #Corresponding radius
    L = Ls[minIndex]    #Corresponding length

    #Re-calculate values
    t1 = p*R/(sigma_y)
    t2 = p*R/(2*sigma_y)
    sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
    Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
    Area = 2* np.pi * R * t1
    sigma = (Fz/Area)/(10**6)


''' Shell Buckling Check'''

if sigma > sigma_cr_shell:
    shell_ind = "Y"
    t1_old = t1
    #Iterate over thickness until it no longer buckles
    while sigma > sigma_cr_shell:
        t1 = t1 + 0.0001

        #Upper boundary on thickness
        if t1 > 0.1 * R:
            print("Change material")
            pg.quit()

        #Update forces and stresses
        Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
        Area = 2* np.pi * R * t1
        sigma = (Fz/Area)/(10**6)

        #Find new critical stress
        sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
            
''' Weight optimisation '''

if shell_ind == "N" and col_ind == "N":
    #Iterate radii between upper and lower boundary.
    #The rest of the process is exactly like column buckling check
    for Ri in np.arange(0.5, 2.2+0.1, 0.01):
        Li = 2/3*Ri+V/(np.pi*Ri*Ri)
        sigma_col = ColBuckle(Ri, Li, E)
        t1i = p*Ri/(sigma_y)
        t2i = p*Ri/(2*sigma_y)
        if Li < 2*Ri + L_min:
            break
        if sigma_col > sigma:
            Rs.append(Ri)
            Ls.append(Li)
            masses.append(TankMass(rho, Ri, Li, t1i, t2i))
            
    massArr = np.array(masses)
    minIndex = np.where(massArr == np.min(massArr))[0][0]
    print(minIndex)
    R = Rs[minIndex]
    L = Ls[minIndex]

    #Re-calculate values
    t1 = p*R/(sigma_y)
    t2 = p*R/(2*sigma_y)

    sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
    Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
    Area = 2* np.pi * R * t1
    sigma = (Fz/Area)/(10**6)

    #Check for shell buckling
    if sigma > sigma_cr_shell:
        t1_old = t1
        while sigma > sigma_cr_shell:
            t1 = t1 + 0.001

            #Upper boundary on thickness
            if t1 > 2 * t1_old :
                print("Change material")
                pg.quit()
            
            #Update forces and stresses
            Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
            Area = 2* np.pi * R * t1
            sigma = (Fz/Area)/(10**6)

            #Find new critical
            sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)

#Print out results
print("Full mass: ", TankMass(rho, R, L, t1, t2))
print("structural mass: ", TankMass(rho, R, L, t1, t2)-39284)
print("R=", R)
print("L=", L)
print("t1=", t1)
print("t2=", t2)
print("sigma=", sigma)
