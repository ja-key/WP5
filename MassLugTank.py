import numpy as np

g = 9.80665
F_z_lug = 1034.5
Launch_load = 6 * g
n = int(input("Pls give number of attachments: "))
m_prop = 39284
m_lug = 1.046   # in grams

ratio = ((m_prop*Launch_load)/n)/F_z_lug

mass_lug_tank = ratio * m_lug
print("One lug mass:", mass_lug_tank, "[g]")
mass_tot = mass_lug_tank * n
print("total mass", mass_tot, "[g]")
