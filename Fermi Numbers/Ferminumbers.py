import numpy as np
import need_cons as nc

mp = nc.mp
q = nc.e_charge
c = nc.c_light
E = 1e18 #ev ankle #1e16 knee
E = nc.ev2ergs(E)
B = 1 #gauss
wl = E/(q*B) #gyro frequency
tesc = 1/wl
Rtm = 1
GB = 15
Rj = 3e18
lamda = Rj*Rtm/GB
ep = 1
alpha=(4/3)*(ep**2)*(c**1)/(lamda)
p=1 + (1/(alpha*tesc))
print(tesc)