from math import pi
p = 21e5  # Pa
R = 1.5  # m
internal_vol = 1.01*32.97  # m^3


L = 2/3*R+internal_vol/(pi*R*R)

print(L)
#             material:Ti-6Al-4V
sigma_yields = np.array([827e6  # Pa


t_1 = p*R/(sigma_yield)
t_2 = p*R/(2*sigma_yield)


print(f"""t_1={t_1*1000} mm, t_2={t_2*1000} mm""")

vol_cylinder = 2*pi*R*t_1*(L-2*R)
print(vol_cylinder)
