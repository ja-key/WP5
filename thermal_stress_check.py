import numpy as np
from forceratio import force_factor
def thermal_force(a_c1,  a_c2, a_b, t_max, t_min, E_b, A_sm, force_ratio):
    F_dtpluslug = (a_c1-a_b)*(t_max-288.15)*E_b*A_sm*(1-force_ratio)
    F_dtminlug = (a_c1-a_b)*(t_min-288.15)*E_b*A_sm*(1-force_ratio)
    F_dtplusskin = (a_c2-a_b)*(t_max-288.15)*E_b*A_sm*(1-force_ratio)
    F_dtminskin = (a_c2-a_b)*(t_min-288.15)*E_b*A_sm*(1-force_ratio)

    return [F_dtpluslug, F_dtminlug, F_dtplusskin, F_dtminskin]


