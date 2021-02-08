from astropy import constants as const

c_light = const.c.cgs.value
h_bar = const.hbar.cgs.value
h = const.h.cgs.value
me = const.m_e.cgs.value
mp = const.m_p.cgs.value
G = const.G.cgs.value
solar_M = const.M_sun.cgs.value

def solarMtoCGS(M):
    return M*solar_M
