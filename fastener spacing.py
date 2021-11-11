def fastener_spacing(D_2, w):
    s_m = (D_2*2, D_2*3)
    s_c = (D_2*4, D_2*5)
    e = 1.5*D_2
    n_m = (w - 2*e)// s_m[0]
    n_c = (w - 2*e)// s_c[0]
    return [n_m, n_c]
