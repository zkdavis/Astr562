from HW11 import  FreidmannUniverse as FU
import numpy as np
from Plotter import Plotter as PL
import need_cons as nc

H_0 = 70*1e5/(nc.parsec2cm(1)*1e9)
def matterdominatedtest(t):
    f = ((3/2)*H_0*t)**(2/3)
    return f

def pr1():
    om = 1
    dst = PL.dataset()
    ds = PL.dataset()
    dst.label="compare"
    t=np.logspace(0,10,100)
    dst.x = t
    dst.y = matterdominatedtest(t)/1e-7
    fu = FU.Friedmann_Universe()
    a,t2 = fu.solveFora()
    t2=np.array(t2)
    t2 = t2/1e10 + t[-1] +2.5e9
    ds.x = t2
    ds.y = a
    pl = PL.Plotter()
    fr = pl.Plot([ds,dst],xscale="linear",yscale="linear")
    fr.pyplt.show()
pr1()
