import numpy as np
import need_cons as nc

#problem 1a
k=0.4
mdot = np.pi*4*nc.G*nc.solar_M/(k*nc.c_light)
#print(mdot)
#problem 1b
tau = nc.solar_M/mdot
#print(nc.num2science(nc.sec2year(tau)))
#problem 2
theta= nc.arcsec2deg((50e-6)/4)
rad = np.deg2rad(theta)
R = nc.lightyears2cgs(53e6)
Rdisk = R*rad
print(nc.num2science(Rdisk))
M_msun = Rdisk/9e5
print(nc.num2science(M_msun*nc.solar_M))