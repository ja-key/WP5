
p = 20e5  # Pa
R = 2  # m
vol = 1.01*32.97  # m^3
t_1 = 1  # mm
t_2 = 1  # mm

sigma_yield = 827e6  # Pa

sigma_axial = p*R/(2*t_1)
sigma_hoop = p*R/(t_2)
