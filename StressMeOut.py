import numpy as np
from ShellBuckling import shellBuckle
from ColumnBuckling import ColBuckle
#Fz =                   # Force in the vertical direction on the tank [N]
R = 1.50                   # Radius in metres of the tank [m]
L = 5.71                   # Total length of the tank in metres [m]
E = 78 * 10**9                   # Young's Modulus of the material [Pa]
v = 0.33                   # Material's poisson ratio []
t1 =  6.43 * 10**(-3)                 # thickness of the straight part of the tank [m]
p =  21 * 10**5                  # internal pressure of the tank [N/m] or [Pa]
t2 =  3.22 * 10**(-3)                 # Thickness of the spherical caps [m]
rho = 2700                 # Density of material used for tank [kg/m^3]
change = "Yes"         # Checks if a variable has changed in previous loop
#R_ult =                # Ultimate boundary for Radius

sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
sigma_cr_col = ColBuckle(R, L, E)
print(sigma_cr_shell)
print(sigma_cr_col)


def TankMass(rho, R, L, t1, t2):
    mass = rho*(2*np.pi*R*t1*(L-2*R) + 4*np.pi*R*R*t2) + 39284
    return mass
Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)

#if sigma_cr_shell > sigma_cr_col:
##    print("The column buckling is more critical")
##    sigma_cr = sigma_cr_col
##elif sigma_cr_col > sigma_cr_shell:
##    print("The shell buckling is more critical")
##    sigma_cr = sigma_cr_shell
##else:
##    print("wow the stresses are the same, good luck")
##    sigma_cr = sigma_cr_shell

Area = 2* np.pi * R * t1
sigma = (Fz/Area)/(10**6)

print("Stress caused by weight is:", sigma)
print(TankMass(rho, R, L, t1, t2)-39284)
print(sigma_cr_shell/sigma)
print(sigma_cr_col/sigma)

t1_upper = (1.05*((TankMass(rho, R, L, t1, t2) - 39284)/rho) - 4*np.pi*R*R*t2)/(2*np.pi*R*(L-2*R))
print(t1_upper)


if sigma > sigma_cr_shell and sigma > sigma_cr_col and change == "Yes":
##    R_new = L/np.pi * np.sqrt(2*sigma/E)
##    shell_new = shellBuckle(p, R_new, L, E, t1, v)
##    pos_check = 1.983*2*t1*E/(R_new*np.sqrt(12*(1-v*v)))
##
##    if shell_new > sigma:
##        R = R_new
##    elif shell_new > pos_check:
##        R=R
##        change = "No"
##        
##    elif sigma > shell_new:
##        while sigma > shell_new and change == "Yes":
##            R_new = R_new + 0.01
##            shell_new = shellBuckle(p, R_new, L, E, t1, v)
##            if R_new > R_ult:
##                change = "No"

Rs = []
Ls = []
masses = []

if sigma > sigma_cr_col:
    L_cr = np.pi*R * np.sqrt(E/(2*sigma))
    for Li in range(L_cr, L):
        Ri = (2*np.pi*t1*Li+ np.sqrt((2*np.pi*t1*Li)**2 - 4*V*(4*np.pi*t1 - 4*np.pi*t2)))/(2*(4*np.pi*t1-4*np.pi*t))
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
    sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
    Fz = 6*9.80665 * TankMass(rho, R, L, t1, t2)
    Area = 2* np.pi * R * t1
    sigma = (Fz/Area)/(10**6)

if sigma > sigma_cr_shell:
    while sigma > sigma_cr_shell:
        t1 = t1 + 0.001
        sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
    
            
##    
####    newList = [R_new, L_new]
####    newNames = ["radius", "length"]
####    
####    mass_R = TankMass(rho, R_new, L, t1, t2)
####    mass _L = TankMass(rho, R, L_new, t1, t2)
####
####    massArr = np.array([mass_R, mass_L])
####    minIndex = np.where(massArr == np.min(massArr))[0]
####
##    print("\nIn order to meet buckling requirement either:\n1) Radius has to be changed to", R_new,"m or \n2) Length has to be changed to", L_new,"m.")
##    for i in minIndex:
##        print("To minimize mass to", massArr[i],"kg, change", newNames[i],"to", newList[i], "m")
##        

else:
    print("WORKS!")

