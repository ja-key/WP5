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

sigma_cr_shell = shellBuckle(p, R, L, E, t1, v)
sigma_cr_col = ColBuckle(R, L, E)

def TankMass(rho, R, L, t1, t2):
    mass = rho*(2*np.pi*R*t1*L + 4*np.pi*R*R*t2)
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

if sigma > sigma_cr_shell:
    
    print("FAILURE")
    print("Stress exceeds the critical buckling stress")
elif sigma > sigma_cr_col:
    print("Fails under column buckling")
    R_new = L/np.pi * np.sqrt(2*sigma/E)
    L_new = np.pi*R * np.sqrt(E/(2*sigma))
    newList = [R_new, L_new]
    newNames = ["radius", "length"]
    
    mass_R = TankMass(rho, R_new, L, t1, t2)
    mass _L = TankMass(rho, R, L_new, t1, t2)

    massArr = np.array([mass_R, mass_L])
    minIndex = np.where(massArr == np.min(massArr))[0]

    print("\nIn order to meet buckling requirement either:\n1) Radius has to be changed to", R_new,"m or \n2) Length has to be changed to", L_new,"m.")
    for i in minIndex:
        print("To minimize mass to", massArr[i],"kg, change", newNames[i],"to", newList[i], "m")
        

else:
    print("WORKS!")

