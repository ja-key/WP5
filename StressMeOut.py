import numpy as np
import ShellBuckling.py
import ColumnBuckling.py
Fz =                   # Force in the vertical direction on the tank [N]
R =                    # Radius in metres of the tank [m]
L =                    # Total length of the tank in metres [m]
E =                    # Young's Modulus of the material [Pa]
v =                    # Material's poisson ratio []
t1 =                   # thickness of the straight part of the tank [m]
p =                    # internal pressure of the tank [N/m] or [Pa]
t2 =                   # Thickness of the spherical caps [m]
rho =                  # Density of material used for tank [kg/m^3]
change = "Yes"         # Checks if a variable has changed in previous loop
R_ult =                # Ultimate boundary for Radius
V
sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
sigma_cr_col = ColBuckle(R, L, E)

def TankMass(rho, R, L, t1, t2):
    mass = rho*(2*np.pi*R*t1*(L-2*R) + 4*np.pi*R*R*t2)
    return mass


##if sigma_cr_shell > sigma_cr_col:
##    print("The column buckling is more critical")
##    sigma_cr = sigma_cr_col
##elif sigma_cr_col > sigma_cr_shell:
##    print("The shell buckling is more critical")
##    sigma_cr = sigma_cr_shell
##else:
##    print("wow the stresses are the same, good luck")
##    sigma_cr = sigma_cr_shell

Area = 2* np.pi * R * t1
sigma = Fz/Area

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
                
elif sigma > sigma_cr_col:
    #R_new = L/np.pi * np.sqrt(2*sigma/E)
    L = np.pi*R * np.sqrt(E/(2*sigma))
    R = (2*np.pi*t1*L+ np.sqrt((2*np.pi*t1*L)**2 - 4*V*(4*np.pi*t1 - 4*np.pi*t2)))/(2*(4*np.pi*t1-4*np.pi*t))
    
##    newList = [R_new, L_new]
##    newNames = ["radius", "length"]
##    
##    mass_R = TankMass(rho, R_new, L, t1, t2)
##    mass _L = TankMass(rho, R, L_new, t1, t2)
##
##    massArr = np.array([mass_R, mass_L])
##    minIndex = np.where(massArr == np.min(massArr))[0]
##
##    print("\nIn order to meet buckling requirement either:\n1) Radius has to be changed to", R_new,"m or \n2) Length has to be changed to", L_new,"m.")
    for i in minIndex:
        print("To minimize mass to", massArr[i],"kg, change", newNames[i],"to", newList[i], "m")
        

else:
    print("WORKS!")

