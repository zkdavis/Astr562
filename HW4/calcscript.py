import  numpy as np
import need_cons as nc

k=0.4
m = nc.solar_M
v=1e7
T0 = np.sqrt(k*m/(v**2))
print(T0)
print(nc.sec2day(T0))