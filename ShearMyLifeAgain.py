import numpy as np


def MemberDes(rho, sigma_y, tau_y, M, Rs, Rt):
    g = 9.80665
    R_t = [] #mm
    Mass = [] #mm
    for n in [12, 16, 20]:
        for theta_deg in range(30, 61):
            # print(n, theta_deg)
            # Calculating member properties
            theta = (theta_deg / 360) * 2 * np.pi  # Angle wrt S/C horizontal, [rad]
            L = (Rs - Rt) / np.cos(theta)  # Length member, [unit of Rs and Rt]

            # Calculating forces in member
            Vy = (M * 6* g * np.cos(theta) + M*2*g*np.sin(theta))/ n  # Shear Force, [N]
            Fx = (M * 6 * g * np.cos(theta) + M * 2 * g * np.sin(theta))/ n  # Tensile Force, [N]

            # Desirable outcome combinations

            for Ri in range(10, 150):  # Desired range for inner radii as determined by the team
                for t in range(1, 50):  # Desired range for thicknesses as determined by the team
                    Ro = Ri + t  # Outer radius, [mm]
                    Ixx = (np.pi / 4) * (Ro ** 4 - Ri ** 4)  # Moment of inertia, [mm^4]
                    Q = 2 / 3 * (Ro ** 3 - Ri ** 3)  # First moment of area, [mm^3]
                    b = 2 * (Ro - Ri)  # Effective thickness, [mm]

                    tau_max = (Vy * Q) / (Ixx * b)  # Shear stress calculations, [MPa]
                    sigma_max = Fx / (np.pi * (Ro ** 2 - Ri ** 2))  # Tensile stress calculations, [MPa]
                    MS_tau = np.absolute(tau_y / tau_max) - 1
##                    print(type(MS_tau))
                    MS_sigma = np.absolute(sigma_y / sigma_max) - 1
##                    print(type(MS_sigma))

                    if MS_tau >= 1 and MS_tau <= 8 and MS_sigma >= 1 and MS_sigma <= 8:
                        MS = min(MS_tau, MS_sigma)
                        print(type(MS))
                        m = (L / 1000) * np.pi * ((Ro / 1000) ** 2 - (Ri / 1000) ** 2) * rho * n
                        print(type(m))
                        print(m)
                        R_t.append([Ro, t, n, theta_deg, round(MS, 2), round(m, 2)])

                        Mass.append(m)

    # Order the massive lists and limit their size
    NewMass = []
    NewR_t = []
    maxvalues = 50
    while len(NewMass) < maxvalues:
        index_min = Mass.index(min(Mass))
        NewMass.append(round(Mass[index_min], 2))
        NewR_t.append(R_t[index_min])
        Mass.pop(index_min)
        R_t.pop(index_min)

    firstval = [x[0] for x in NewR_t]
    RadiiMass = []
    RadiiR_t = []
    maxvaluesRadii = 10
    while len(RadiiMass) < maxvaluesRadii:
        index_minRadius = firstval.index(min(firstval))
        RadiiMass.append(NewMass[index_minRadius])
        RadiiR_t.append(NewR_t[index_minRadius])
        firstval.pop(index_minRadius)
        NewMass.pop(index_minRadius)
        NewR_t.pop(index_minRadius)

##    print("R_outer [mm], t [mm], n [-], theta [deg], M.S. [-], mass [kg]")
##    print(RadiiR_t)
    return [RadiiR_t[0][0], RadiiR_t[0][5]]


M = 877.53+39284 # kg 40163.22
E = 6.8 * 10 ** 10
rho = 2.5 * 10 ** 3
sigma_y = 3 * 10 ** 1
tau_y = 207
Rs = 2500
Rt = 1930
# n = 20

##x = MemberDes(rho, sigma_y, tau_y, M, Rs, Rt)
##print(x)




























