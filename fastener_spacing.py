import numpy as np

def D2(w, s): #only w is limiting for the hole diameter since the lug is wider than it is tall
    D2 = w/(s+3)
    return D2

def fastener_spacing(D_2, w, L):
    x_pos = np.array([1.5*D_2, L-1.5*D_2])
    z_pos = np.array([1.5*D_2, w-1.5*D_2])
    x_avg = np.average(x_pos)
    z_avg = np.average(z_pos)

    return [x_pos, z_pos, x_avg, z_avg]

#temporarily commented out for simplicity

#def fastener_spacing(D_2, w, c, Br, s):   #D_2 is the hole diameter, w is the width of the flanges, c is the amount of columns on each side. Br is the total width of the lug. S is the relative spacing compared to the hole size
    #spacing = s*D_2
   # n = (w-3*D_2)//spacing
    #e = (w-n*spacing)/2
    #print(n)
    #print(e)


   # x_pos = np.arange(e, e+n*spacing, spacing)
   # y_posleft = np.arange(D_2*1.5, c*spacing + D_2, spacing)
   # y_posright = np.arange(Br-(c*spacing-D_2*1.5), Br-D_2*1.5, spacing)
   # y_pos = np.append(y_posleft, y_posright)
  #  x_avg = np.average(x_pos)
    #y_avg = np.average(y_pos)
    #return [y_pos, x_pos, y_avg, x_avg]
