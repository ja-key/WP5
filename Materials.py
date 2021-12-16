from math import pi
import numpy as np

p = 21e5  # Pa
R = 1.5  # m
internal_vol = 1.01*32.97  # m^3


L = 2/3*R+internal_vol/(pi*R*R)

internal_vol = L*pi*R*R - 2/3*pi*R*R*R
print(L)
materials = np.array(['Ti-6Al-4V', 'AA2195-T84', 'AA2219-T87', 'CFRP'])
sigma_yields = np.array([827e6, 490e6, 395e6])  # Pa
rhos = np.array([4430, 2700, 2840])

sigma_cfrp_lam_0 = 2703e6
sigma_cfrp_lam_90 = 81e6
rho_cfrp = 1770


t_1s = p*R/(sigma_yields)
t_2s = p*R/(2*sigma_yields)

t1_cfrp = p*R/(sigma_cfrp_lam_0)+p*R/(2*sigma_cfrp_lam_0)
t2_cfrp = p*R/(2*sigma_cfrp_lam_0)

print(f"""t_1={t_1s*1000} mm, t_2={t_2s*1000} mm""")

vol_tanks = 2*np.pi*R*t_1s*(L-2*R) + 4*np.pi*R*R*t_2s

vol_cfrp = 2*np.pi*R*t1_cfrp*(L-2*R) + 4*np.pi*R*R*t2_cfrp
#print(vol_tanks)

for i in range(len(list(vol_tanks))):
    print(f"mass of tank {materials[i]} = {vol_tanks[i]*rhos[i]} kg")

print(f"""t_1_cfrp={t1_cfrp*1000} mm, t2_cfrp={t2_cfrp*1000} mm""")
print(f"mass of CFRP tank = {vol_cfrp*rho_cfrp} kg")
