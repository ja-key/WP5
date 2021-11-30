import numpy as np

def force_factor(D_fo, D_fi, E_a, E_b, t2, t3):
    d = D_fi
    print("Please define your desired configuration:")
    print("Please give me head:")
    head = input("Hexagon (1) or Cylindrical Head (2) :")
    if "1" or "hex" in head.lower():
        head = 0.5 * d
    else:
        head = 0.4 * d

    print("Please give me an engaged shank")
    shank = input("Nut (1) or threaded (2) :")
    if "1" or "nut" in shank.lower():
        shank = 0.4 * d
    else:
        shank = 0.33*d
    lock = 0.4 * d
    A = np.pi * (d/2)**2
    delta_b = (1/E_b) * ((head/ A) + (shank/A) + (lock/A) + ((t2+t3)/A))

    delta_a1 = (4 * t2) / (E_a * np.pi * (D_fo ** 2 - D_fi ** 2))
    delta_a2 = (4 * t3) / (E_a * np.pi * (D_fo ** 2 - D_fi ** 2))
    t_ratio = t2/(t3+t2)
    F_ratio = float(t_ratio*(delta_a1 / (delta_a1 + delta_b)) + (1-t_ratio)*(delta_a2 / (delta_a2 + delta_b)) )
    print("Sir, thy requested force ration is:", F_ratio)
    return F_ratio