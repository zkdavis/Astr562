import ModelFitter.ModelFitter as MF
from ModelFitter.ModelFitter import dataform as df
from Plotter.Plotter import dataset,figret
import Plotter.Plotter as PL
import numpy as np
import need_cons as nc


delta_t= 0.11
v=1.3e9
v1 = 1.4e9
v2 = 1.2e9

Re=(nc.e_charge**2)/(nc.me*(nc.c_light**2))
dm = delta_t*(v**3)*np.pi/(Re*nc.c_light*(v1-v2))
pc = nc.parsec2cm(1)
dm=dm#/pc
dm=146*pc
print(dm)
D=8e7
n=dm/D
Mt=nc.me*dm*(D**2)
print(nc.num2science(Mt))
print(nc.num2science(Mt/nc.solar_M))
print("n: "+str(nc.num2science(n)))
# print(nc.num2science(dm))
# F=1e10
# d=1.46e8
# dt = 2.46e-3
# d=nc.parsec2cm(d)
# u=F*(d**2)
# print(nc.num2science(u))