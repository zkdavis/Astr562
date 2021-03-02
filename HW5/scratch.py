import numpy as np
import need_cons as nc

R=nc.AU2cm(100)
GM = nc.solar_M*nc.G
h_r=0.1
k=0.4
alpha=0.01
tau_C = np.sqrt((R**3)/GM)*((1/h_r)**2)*(1/alpha)
t_y = nc.sec2year(tau_C)
# print(t_y)
# print(tau_C)
M=1e9*nc.solar_M
bsig=((1/h_r)**2)*np.sqrt(nc.G)*nc.solar_M/(k*alpha*nc.c_light*9e5*np.sqrt(M))
# print(nc.num2science(bsig))
mg = ((1/h_r)**2)*np.sqrt(nc.G*M)*9e6*(M/nc.solar_M)/(k*alpha*nc.c_light)
# print(nc.num2science(mg/nc.solar_M))
jm = nc.solar_M/1e3
bigsig=jm/(nc.AU2cm(100)**2)
L = nc.L_solar
sb = nc.sig_sb
R=nc.AU2cm(1)
T=(bigsig*k*L/(sb*4*np.pi*(R**2)))**(1/4)
omega = np.sqrt(GM/(R**3))
h_R = ((T*nc.k_boltz/nc.mp)**(1/2))*(1/(R*omega))
print(nc.num2science(T))
print(nc.num2science(h_R))