import numpy as np

def fastener_spacing(D_2, w, c, Br, s):   #D_2 is the hole diameter, w is the width of the flanges, c is the amount of columns on each side. Br is the total width of the lug. S is the relative spacing compared to the hole size
    spacing = s*D_2
    n = (w-3*D_2)//spacing
    e = (w-n*spacing)/2

    x_pos = np.arange(e, e+n*spacing, spacing)
    y_posleft = np.arange(D_2*1.5, c*spacing + D_2, spacing)
    y_posright = np.arange(Br-(c*spacing-D_2*1.5), Br-D_2*1.5, spacing)
    y_pos = np.append(y_posleft, y_posright)

    return [y_pos, x_pos]
