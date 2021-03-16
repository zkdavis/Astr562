import numpy as np
import need_cons as nc
import need_plots as PL

def GB_nonR(E,rho,t,tjet=None,theta=None):
    if tjet is None:
        t = nc.day2sec(t)
        f = (E/(rho*(nc.c_light**5)*(t**3)))**(1/5)
        return f
    else:
        # ftemp = (E / (rho * (nc.c_light ** 5) * (t ** 3))) ** (1 / 5)
        # tjet = np.argmin(np.abs(ftemp - theta))
        t2 = nc.day2sec(t)[tjet:]
        t1 = nc.day2sec(t)[:tjet]
        f1 = (E/(rho*(nc.c_light**5)*(t1**3)))**(1/5)
        f2 = ((E*(theta**2))/(rho*(nc.c_light**5)*(t2**3)))**(1/5)
        f = np.append(f1,f2)
        return f

def GB_R_t(E,rho,t,tjet=None,theta=None):
    if tjet is None:
        t = nc.day2sec(t)
        f = (E/(rho*(nc.c_light**5)*(t**3)))**(1/2)
        return f
    else:
        # ftemp = (E / (rho * (nc.c_light ** 5) * (t ** 3))) ** (1 / 2)
        # tjet = np.argmin(np.abs(ftemp - theta))
        t2 = nc.day2sec(t)[tjet:]
        t1 = nc.day2sec(t)[:tjet]
        f1 = (E / (rho * (nc.c_light ** 5) * (t1 ** 3))) ** (1 / 2)
        f2 = ((E*(theta**2)) / (rho * (nc.c_light ** 5) * (t2 ** 3))) ** (1 / 2)
        f = np.append(f1, f2)
        return f
def GB_R_tobs(E,rho,t,tjet=None,theta=None):
    if tjet is None:
        t=nc.day2sec(t)
        f = (E/(rho*(nc.c_light**5)*(t**3)))**(1/8)
        return f
    else:
        # ftemp = (E / (rho * (nc.c_light ** 5) * (t ** 3))) ** (1 / 8)
        # tjet = np.argmin(np.abs(ftemp-theta))
        t2 = nc.day2sec(t)[tjet:]
        t1 = nc.day2sec(t)[:tjet]
        f1 = (E / (rho * (nc.c_light ** 5) * (t1 ** 3))) ** (1 / 8)
        f2 = ((E*(theta**2)) / (rho * (nc.c_light ** 5) * (t2 ** 3))) ** (1 / 8)
        f = np.append(f1, f2)
        return f

def Full_GB_t(E,rho,t,tjet=None,theta=None):

    f1 = GB_R_t(E, rho, t,tjet,theta)
    f2 = GB_nonR(E,rho,t,tjet,theta)
    index=np.argmin(np.abs(f2-f1))
    f = f1[:index]
    f = np.append(f, f2[index:])
    return f


def Full_GB_tobs(E, rho, t,tjet=None,theta=None):
    f1 = GB_R_tobs(E, rho, t,tjet,theta)
    f2 = GB_nonR(E, rho, t,tjet,theta)
    index = np.argmin(np.abs(f2-f1))
    f = f1[:index]
    f = np.append(f,f2[index:])
    return f

# ds = PL.dataset()
# ds2 = PL.dataset()
# ds3 = PL.dataset()
# E=1e53
# t = np.logspace(-4,2,100)
# #t = nc.day2sec(t)
# rho = nc.mp/(1e-6)
#
# ds.x=t
# ds2.x=t
# ds.label="$\Gamma (t)$"
# ds2.label="$\Gamma (t_{obs})$"
# theta=0.1
# ts = nc.day2sec(t)
# tj = (((theta**8)*E)/(rho*(nc.c_light**5)))**(1/3)
# #tj = nc.sec2day(tj)
# t0 = (E/(rho*(nc.c_light**5)))
# t0 = nc.sec2day(t0)
# tjind = np.argmin(np.abs(ts-tj))
# y1 = Full_GB_t(E,rho,t,tjet=tjind,theta=theta)
# #y1 =GB_R_t(E,rho,t)
# y2 = Full_GB_tobs(E,rho,t,tjet=tjind,theta=theta)
# #y2 = GB_R_tobs(E,rho,t)
# ds.y = y1
# ds2.y=y2
# ds3.x = t
# ds3.y = GB_nonR(E,rho,t)
#
# pl = PL.Plotter()
# fr = pl.Plot([ds,ds2],title="",xlabel="Days",ylable=r"$\Gamma \beta$")
# fr.pyplt.show()
