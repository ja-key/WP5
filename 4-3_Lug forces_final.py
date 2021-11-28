import numpy as np

#Design parameters of the attaching frame
r = 0.15     #half of the width of the attachment, [m]
h = 0.49    #half of the length of the attachment, [m]
a = 0.1     #distance of clearance needed because of the fins of the RTG, [m]
theta = 60  #angle z,y-plane CCW wrt +z-axis [deg]
beta = 70   #angle x,y-plane CCW wrt +x-axis [deg]
#Forces intruduced by the RTG
F_lat_x = 1036  #Lateral launch load in x-direction, [N]
F_lat_y = 1036  #Lateral launch load in y-direction, [N]
W = 3107        #weight of the RTG during launch, [N]
def reactionforces(r, h, a, theta, beta, F_lat_x, F_lat_y, W):
    y = a
    x = y/np.tan(theta/180*np.pi)
    z = y/np.tan(beta/180*np.pi)

    l_vector = np.sqrt(y**2 + x**2 + z**2)
    yu = y/l_vector
    xu = x/l_vector
    zu = z/l_vector

    Matrix = np.array([[xu, -xu, xu, -xu],
                       [yu, yu, yu, yu],
                       [-zu, -zu, zu, zu],
                       [-xu*h+zu*r, xu*h-zu*r, xu*h-zu*r, -xu*h+zu*r]])

    equalto = np.array([[-F_lat_x], [-F_lat_y], [W], [0]])
    solution = np.linalg.solve(Matrix, equalto)
    print(solution)

    Ps = ( solution**2 )**0.5 #to make it absolute values
    Ps = np.ceil(Ps)
    P = max(Ps) #Evaluate the maximum force a lug will endure (compression is taken into account as well)
    return(P, xu*P, yu*P, zu*P)


Pxyz = reactionforces(r, h, a, theta, beta, F_lat_x, F_lat_y, W)
print(Pxyz)
