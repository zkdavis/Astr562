import numpy as np
import scipy.integrate as integrate
import need_cons as nc
import need_plots as pl
import data_reader as dr

plots = pl.Plotter()

def x_ni(t,x0):
    #l=1/nc.day2sec(6.10)
    l=1/6.10
    f= x0*np.exp(-l*t)
    return f

def x_co(t,x0):
   # lni = 1 / nc.day2sec(6.10)
    lni = 1 / 6.10
    #l=1/nc.day2sec(77.12)
    l=1/77.12
    f= (lni*x0/(l-lni))*(np.exp(-lni*t) - np.exp(-l*t))
    return f

def dE_ni(t,x0):
    ee=nc.ev2ergs(1.75e6)
    f=x_ni(t,x0)*ee
    return f

def dE_co(t,x0):
    f=x_co(t,x0)*nc.ev2ergs(3.73e6)
    return f
def L_heat_ni_co(t,x0):
    f=dE_ni(t,x0)+dE_co(t,x0)
    return f
def L_heat_ni_co_simplified(t):
    x0=5e36
    f=dE_ni(t,x0)+dE_co(t,x0)
    return f

def L_heat(t):
    L0=1
    f=L0
    return f

def Lheat_int(Lh,t,T0):
    intf = lambda x: Lh(x)*x*np.exp(0.5*((x/T0)**2))
    #f = integrate.romberg(intf,0,t)
    #f = integrate.romberg(intf,0,t,tol=1e-10,rtol=1e-10,divmax=100)
    f = integrate.quad(intf,0,t)
    return f[0]

def E_therm(Lheat,t,T0):
    f=(np.exp(-0.5*((t/T0)**2))/t)*Lheat_int(Lheat,t,T0)
    return f
def L_out(lh,t,T0):
    f=(np.exp(-0.5*((t/T0)**2))/(T0**2))*Lheat_int(lh,t,T0)
    return f
def L_out_check(t,T0,L0):
    f = L0*(1 - np.exp(-0.5*((t/T0)**2)))
    return -f

def pr2():
    t=np.logspace(0,0.7,100)
    y=[]
    y2=L_out_check(t,1,1)
    for i in t:
        y.append(L_out(L_heat,i,1))
    ds = pl.dataset()
    ds2 = pl.dataset()
    ds.x=t
    ds.label="Python integration L0=1 T0=1"
    ds2.label="Analytical solution L0=1 T0=1"
    ds.y=y
    #ds.plot_type = ds.plottype
    ds2.plot_type = ds2.plottype
    ds.marker_size=15
    ds.color="C2"
    ds2.x=t
    ds2.y=y2
    fr = plots.Plot(datasets=[ds,ds2],title="$L_{out}$",xscale="log",yscale="log",xlabel="t",ylable="L")
    fr2 = plots.Plot(datasets=[ds,ds2],title="$L_{out}$",xscale="linear",yscale="linear",xlabel="t",ylable="L")
    fr.pyplt.show()

def pr3c():
    t=np.logspace(0,7,1000)
    y=dE_ni(t,1)
    y3 = dE_co(t,1)
    y2=L_heat_ni_co(t,1)
    ds = pl.dataset()
    ds2 = pl.dataset()
    ds3 = pl.dataset()
    ds.x=t
    ds.label="From Ni"
    ds3.label="From Co"
    ds2.label="Total"
    ds.y=y
    ds3.x=t
    ds3.y=y3
    ds.marker="--"
    ds3.marker="--"
    ds3.plot_type=ds3.plottype
    ds.plot_type = ds.plottype
    ds2.plot_type = ds2.plottype
    ds.marker_size=15
    ds2.x=t
    ds2.y=y2
    fr2 = plots.Plot(datasets=[ds,ds3,ds2],title="$L_{out}$  From Ni and Co [ergs/s]",xscale="linear",yscale="linear",xlabel="t [s]",ylable="L")
    fr2.pyplt.show()

def pr3d():
    t=np.linspace(0,100,100)
    y=[]
    k=0.4
    m = nc.solar_M
    v=1e7
    T0 = np.sqrt(k*m/(v**2))
    T0 = nc.sec2day(T0)
    T0=T0*1e-4
    for i in t:
        y.append(L_out(L_heat_ni_co_simplified,i,T0))
    ds = pl.dataset()
    y2=L_heat_ni_co_simplified(t)
    ds2=pl.dataset()
    ds3=pl.dataset()
    dt = dr.getdata()
    tx = dt[0]
    ty=dt[1]
    ds3.x =np.array(tx) #nc.day2sec(tx)
    tty=[]
    for i in ty:
        tty.append(nc.MBtolum(i))
    ds3.y =np.array(tty)
    ds2.x=t
    ds2.y=y2
    ds2.label="Ni_Co _heating"
    ds2.marker_size=7
    ds.x=t
    ds.label="Lout"
    ds.y=y
    ds.plot_type = ds.plottype
    #ds.marker_size=15
    ds.color="C2"
    fr = plots.Plot(datasets=[ds,ds2,ds3],title="$L_{out}$ [erg/s]",xscale="linear",yscale="linear",xlabel="t [days]",ylable="L")
    #fr2 = plots.Plot(datasets=[ds3],title="$L_{out}$",xscale="linear",yscale="linear",xlabel="t",ylable="L")
    fr.pyplt.show()
    #fr.fig.show()
#pr3d()

class p4:
    def __init__(self):
        self.x0=None
        self.T0=None

    def x_ni(self, t, x0):
        # l=1/nc.day2sec(6.10)
        l = 1 / 6.10
        f = x0 * np.exp(-l * t)
        return f

    def x_co(self,t, x0):
        # lni = 1 / nc.day2sec(6.10)
        lni = 1 / 6.10
        # l=1/nc.day2sec(77.12)
        l = 1 / 77.12
        f = (lni * x0 / (l - lni)) * (np.exp(-lni * t) - np.exp(-l * t))
        return f

    def dE_ni(self,t, x0):
        ee = nc.ev2ergs(1.75e6)
        f = self.x_ni(t, x0) * ee
        return f

    def dE_co(self,t, x0):
        f = self.x_co(t, x0) * nc.ev2ergs(3.73e6)
        return f

    def L_heat_ni_co(self,t, x0):
        f = self.dE_ni(t, x0) + self.dE_co(t, x0)
        return f

    def L_heat_ni_co_simplified(self,t):
        x0 = self.x0
        f = self.dE_ni(t, x0) + self.dE_co(t, x0)
        return f

    def L_heat(self,t):
        L0 = 1
        f = L0
        return f

    def Lheat_int(self,Lh, t, T0):
        intf = lambda x: Lh(x) * x * np.exp(0.5 * ((x / T0) ** 2))
        # f = integrate.romberg(intf,0,t)
        # f = integrate.romberg(intf,0,t,tol=1e-10,rtol=1e-10,divmax=100)
        f = integrate.quad(intf, 0, t)
        return f[0]

    def E_therm(self,Lheat, t, T0):
        f = (np.exp(-0.5 * ((t / T0) ** 2)) / t) * Lheat_int(Lheat, t, T0)
        return f

    def L_out(self,lh, t, T0):
        f = (np.exp(-0.5 * ((t / T0) ** 2)) / (T0 ** 2)) * Lheat_int(lh, t, T0)
        return f

    def L_out_check(self,t, T0, L0):
        f = L0 * (1 - np.exp(-0.5 * ((t / T0) ** 2)))
        return f