import numpy as np

def MemberDes(rho, sigma_y, tau_y, W, theta, Rs, Rt, n):
#inputs
# Rs is the radius of spacecraft amd Rt is the radius of tank
# W = float(input("Weight"))
# theta = float(input('Theta (degrees)'))
# theta = (theta /360) *2 * np.pi
    i =0
    theta = (theta/360)*2 * np.pi
    Vy = W * np.cos(theta) / n #Shear Force, [N]
    Fx = W * np.cos(theta) / n
    L = (Rs-Rt)/np.cos(theta)
    R_t = []
    Mass = []
    for Ri in range(10, 150):
        for t in range(1, 50):
            Ro =  Ri + t #outer radius, [m]
            Ixx = (np.pi/4) * (Ro**4 - Ri**4)
            Q = 2/3 * (Ro**3 - Ri**3)  #first moment of area
            b = 2 * (Ro - Ri)    # effective thickness ?

            tau_max = (Vy * Q) / (Ixx * b)   #Shear flow calculations MPa
            sigma_max = Fx/(np.pi * (Ro**2-Ri**2)) #MPa
            MS_tau = np.absolute(tau_y / tau_max) - 1
            MS_sigma = np.absolute(sigma_y / sigma_max) - 1
            print(MS_tau, MS_sigma)

            if MS_tau >= 0.5 and MS_tau <= 5 and MS_sigma >= 0.5 and MS_sigma <=5:
                MS = min(MS_tau, MS_sigma)
                R_t.append([Ro, t, round(MS, 2)])
                m = (L/1000) * np.pi * ((Ro/1000)**2-(Ri/1000)**2) *rho
                Mass.append(m)

            i = i+1

    return( R_t, Mass)


W = 39000 * 6 * 9.80665
E = 6.8*10**10
rho = 2.5*10**3
sigma_y = 3*10**1
tau_y = 207
theta = 60
Rs = 2500
Rt = 1500
n = 20


x0 = MemberDes(rho, sigma_y, tau_y, W, theta, Rs, Rt, n)[0]
x1 = MemberDes(rho, sigma_y, tau_y, W, theta, Rs, Rt, n)[1]

print(x0)
print(x1)

h = x1.index(min(x1))
print("Mass:", x1[h])
print("Dimensions:", x0[h])
print(len(x0))

NewMass = []
NewR_t = []


while len(x0)>0:
    index_min = x1.index(min(x1))
    NewMass.append(round(x1[index_min], 2))
    NewR_t.append(x0[index_min])
    x1.pop(index_min)
    x0.pop(index_min)

print(NewR_t)
print(NewMass)







