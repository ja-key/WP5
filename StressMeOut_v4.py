import numpy as np
from ShellBuckling import shellBuckle
from ColumnBuckling import ColBuckle

R = 1.50                   # Radius in metres of the tank [m]
L = 5.71                   # Total length of the tank in metres [m]
E = 78 * 10**9                   # Young's Modulus of the material [Pa]
v = 0.33                   # Material's poisson ratio []
t1 =  6.43 * 10**(-3)                 # thickness of the straight part of the tank [m]
p =  21 * 10**5                  # internal pressure of the tank [N/m] or [Pa]
t2 =  3.22 * 10**(-3)                 # Thickness of the spherical caps [m]
rho = 2700                 # Density of material used for tank [kg/m^3]
sigma_y = 490e6           #yield stress of material [Pa]
col_ind = "N"         # Checks if a variable has changed in previous loop
shell_ind = "N"
mAttatch = 0          #Mass of the attatchments

''' Initial parameters for Titanium '''
##E = 114 * 10**9                   # Young's Modulus of the material [Pa]
##t1 =  3.81 * 10**(-3)                 # thickness of the straight part of the tank [m]
##t2 =  1.91 * 10**(-3)                 # Thickness of the spherical caps [m]
##rho = 4430                 # Density of material used for tank [kg/m^3]
##sigma_y = 827e6           #yield stress of material [Pa]

sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
sigma_cr_col = ColBuckle(R, L, E)

def TankMass(rho, R, L, t1, t2):
    mass = rho*(2*np.pi*R*t1*(L-2*R) + 4*np.pi*R*R*t2) + 39284 + mAttatch
    return mass
print("mass is", TankMass(rho, R, L, t1, t2))

V = 33.3    #Volume in [m^3]

Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
Area = 2* np.pi * R * t1
sigma = (Fz/Area)/(10**6)

Rs = []
Ls = []
masses = []

if sigma > sigma_cr_col:
    col_ind = "Y"
    R_old = R
    R_cr = L/np.pi * np.sqrt((2*sigma)/E)
    for Ri in np.arange(R, R_cr, 0.01):
        Li = -4/3*Ri+V/(np.pi*Ri*Ri)
        sigma_col = ColBuckle(Ri, Li, E)
        if sigma_col > sigma:
            Rs.append(Ri)
            Ls.append(Li)
            masses.append(TankMass(rho, Ri, Li, t1, t2))
    massArr = np.array(masses)
    minIndex = np.where(massArr == np.min(massArr))[0]
    R = Rs[minIndex]
    L = Ls[minIndex]

    #Re-calculate values
    t1 = p*R/(sigma_y)
    t2 = p*R/(2*sigma_y)
    sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
    Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
    Area = 2* np.pi * R * t1
    sigma = (Fz/Area)/(10**6)


if sigma > sigma_cr_shell:
    shell_ind = "Y"
    t1_old = t1
    while sigma > sigma_cr_shell:
        t1 = t1 + 0.0001

        #Update forces and stresses
        Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
        Area = 2* np.pi * R * t1
        sigma = (Fz/Area)/(10**6)

        #Find new critical
        sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
            
print("Has it failed in Col?", col_ind,)
print("Has it failed in Shell?", shell_ind)

if shell_ind == "N" and col_ind == "N":
##    R_cr = L/np.pi * np.sqrt((2*sigma)/E)
##    print("R_cr =", R_cr)
##    if R_cr < 0.5:
##        R_cr = 0.5
##    print("R_cr is changed to:", R_cr)
    for Ri in np.arange(0.5, 2.2+0.1, 0.01):
        print("Ri= ", Ri)
        Li = 2/3*Ri+V/(np.pi*Ri*Ri)
        print("Li =", Li)
        sigma_col = ColBuckle(Ri, Li, E)
        t1i = p*Ri/(sigma_y)
        t2i = p*Ri/(2*sigma_y)
        if Li < 2*Ri:
            break
        if sigma_col > sigma:
            Rs.append(Ri)
            Ls.append(Li)
            print("mass is", TankMass(rho, Ri, Li, t1i, t2i))
            masses.append(TankMass(rho, Ri, Li, t1i, t2i))
            
    massArr = np.array(masses)
    #print(massArr)
    #print(Rs)
    #print(Ls)
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
    print("R=", R)
    print("L=", L)
    print("t1=", t1)
    print("t2=", t2)
    print("sigma=", sigma)

    if sigma > sigma_cr_shell:
        t1_old = t1
    while sigma > sigma_cr_shell:
        t1 = t1 + 0.001

        #Update forces and stresses
        Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
        Area = 2* np.pi * R * t1
        sigma = (Fz/Area)/(10**6)

        #Find new critical
        sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
            

elif shell_ind == "N" and col_ind == "Y":
    col_ind = "N"

elif shell_ind == "Y" and col_ind == "N":
    t1s = []
    L_cr = np.pi*R * np.sqrt(E/(2*sigma))
    for Li in np.arange(L, L_cr, 0.01):
        for ti in np.arange(t1_old, t1, 0.0001):
            Ri = (2*np.pi*ti*Li+ np.sqrt((2*np.pi*ti*Li)**2 - 4*V*(4*np.pi*ti - 4*np.pi*t2)))/(2*(4*np.pi*ti-4*np.pi*t))
            sigma_col = ColBuckle(Ri, Li, E)
            sigma_shell = shellBuckle(p, Ri, Li, E, ti, v)
            sigma_pr = p*Ri/(ti)

            Fz = 6*9.80665 * TankMass(rho, Ri, Li, ti, t2)
            Area = 2* np.pi * Ri * ti
            sigma = (Fz/Area)/(10**6)
            
            if sigma_col > sigma and sigma_shell > sigma and sigma_y > sigma_pr:
                Rs.append(Ri)
                Ls.append(Li)
                t1s.append(ti)
                masses.append(TankMass(rho, Ri, Li, ti, t2))
    massArr = np.array(masses)
    minIndex = np.where(massArr == np.min(massArr))[0]
    R = Rs[minIndex]
    L = Ls[minIndex]
    t1 = t1s[minIndex]

    t2 = p*R/(2*sigma_y)
    Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
    Area = 2* np.pi * R * t1
    sigma = (Fz/Area)/(10**6)
    shell_ind = "N"

else:
    t1s = []
    L_cr = np.pi*R * np.sqrt(E/(2*sigma))
    for Li in range(L_cr, L_old, 0.01):
        for ti in range(t1_old, t1, 0.0001):
            Ri = (2*np.pi*ti*Li+ np.sqrt((2*np.pi*ti*Li)**2 - 4*V*(4*np.pi*ti - 4*np.pi*t2)))/(2*(4*np.pi*ti-4*np.pi*t))
            sigma_col = ColBuckle(Ri, Li, E)
            sigma_shell = shellBuckle(p, Ri, Li, E, ti, v)
            sigma_pr = p*Ri/(ti)

            Fz = 6*9.80665 * TankMass(rho, Ri, Li, ti, t2)
            Area = 2* np.pi * Ri * ti
            sigma = (Fz/Area)/(10**6)
            
            if sigma_col > sigma and sigma_shell > sigma and sigma_y > sigma_pr:
                Rs.append(Ri)
                Ls.append(Li)
                t1s.append(ti)
                masses.append(TankMass(rho, Ri, Li, ti, t2))
    massArr = np.array(masses)
    minIndex = np.where(massArr == np.min(massArr))[0]
    R = Rs[minIndex]
    L = Ls[minIndex]
    t1 = t1s[minIndex]

    t2 = p*R/(2*sigma_y)
    Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
    Area = 2* np.pi * R * t1
    sigma = (Fz/Area)/(10**6)
    shell_ind = "N"
    col_ind = "N"

