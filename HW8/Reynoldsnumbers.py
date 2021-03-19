import numpy as np
import need_cons as nc

c = ((nc.e_charge)**2)*((nc.me)**(1/2))/(nc.mp*((nc.k_boltz)**(5/2)))

def schR(M):
    return 2*nc.G*M/((nc.c_light)**2)

def Reynolds_number(m,v,l,T):
    return c*(m*v/((l**2)*(T**(5/2))))
#accretion disk
# m=1e1*nc.solar_M
# r = schR(m)*10
# v=r*np.sqrt(nc.G*m/r**3)
# T= (nc.G*m*nc.mp*nc.c_light/(nc.sig_sb*nc.sig_t*(r**2)))**(1/4)
# re = Reynolds_number(m,v,r,T)
#ism
l = nc.parsec2cm(2000)
r = 1.8e15
m = (1e-3)*nc.mp*(l*(r**2))
v=r*np.sqrt(nc.G*m/r**3)
T=1e6
re = Reynolds_number(m,v,r,T)


print(nc.num2science(re))