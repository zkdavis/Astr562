from HW11 import  FreidmannUniverse as FU
import numpy as np
from Plotter import Plotter as PL
import need_cons as nc

H_0 = 70*1e5/(nc.parsec2cm(1)*1e6)
def matterdominatedtest(t):
    f = ((3/2)*H_0*t)**(2/3)
    return f

def testpr3(t,om,ol):
    f = ((om/ol)**(1/3))*(np.sinh(t/3.5e17)**(2/3))
    return f

def pr1():
    om = 1
    dst = PL.dataset()
    ds = PL.dataset()
    dst.label=r"$a=\left(\frac{3}{2}H_{0} t \right)^\frac{2}{3} $"
    ds.label="numerical"

    fu = FU.Friedmann_Universe()
    a,t2 = fu.solveFora2()
    t2=np.array(t2)
    t2 = t2 + max(-t2)
    #t2 = np.flip(-t2)
    t2=np.append(t2,[t2[-1]])
    a = np.append(a,[0])
    t=np.linspace(0,max(t2),100)
    y = matterdominatedtest(t)

    dst.x = t
    dst.y = y
    ds.x = t2
    ds.y = a
    pl = PL.Plotter()
    fr = pl.Plot([ds,dst],xscale="linear",yscale="linear",xlabel="t [s]",ylable="a(t)",title="Matter Dominated Universe")
    fr.ax.xaxis.label.set_size(20)
    fr.ax.yaxis.label.set_size(20)
    fr.ax.tick_params(labelsize=20)
    handles, labels = fr.ax.get_legend_handles_labels()
    fr.ax.legend(handles, labels, loc="best", prop={'size': 20})
    fr.pyplt.show()

def pr2():
    dst = PL.dataset()
    ds = PL.dataset()
    dst.label=r"$a=\left(\frac{3}{2}H_{0} t \right)^\frac{2}{3} $"
    ds.label="numerical"

    fu = FU.Friedmann_Universe()
    fu.omega_M=0
    fu.omega_lambda=1
    a,t2 = fu.solveFora2()
    t2=np.array(t2)
    t2 = t2 + max(-t2)

    t=np.linspace(0,max(t2),100)
    dst.x = t
    dst.y = matterdominatedtest(t)
    ds.x = t2
    ds.y = a
    pl = PL.Plotter()
    fr = pl.Plot([ds,dst],xscale="linear",yscale="linear",xlabel="t [s]",ylable="a(t)",title="Vacuum Dominated Universe")
    fr.ax.xaxis.label.set_size(20)
    fr.ax.yaxis.label.set_size(20)
    fr.ax.tick_params(labelsize=20)
    handles, labels = fr.ax.get_legend_handles_labels()
    fr.ax.legend(handles, labels, loc="best", prop={'size': 20})
    fr.pyplt.show()

def pr3():
    dst = PL.dataset()
    ds = PL.dataset()
    dst.label=r"$a=\left(\frac{\Omega_{M}}{\Omega_{\Lambda}}\right)^\frac{1}{3} \left(\sinh(\frac{t}{t_{\Lambda}})\right)^\frac{2}{3} $ with $t_{\Lambda}$ = 3.5e17 "
    ds.label="numerical"

    fu = FU.Friedmann_Universe()
    fu.omega_M=0.29
    fu.omega_lambda=0.71
    a,t2 = fu.solveFora2()
    t2=np.array(t2)
    t2 = t2 + max(-t2)

    t=np.linspace(0,max(t2),100)
    dst.x = t
    y=testpr3(t,0.29,0.71)
    for i in range(len(y)):
        if y[i]>1e1:
            y[i]=1
    dst.y = y
    t2 = np.append(t2, [t2[-1]])
    a = np.append(a, [0])
    ds.x = t2
    ds.y = a
    pl = PL.Plotter()
    fr = pl.Plot([ds,dst],xscale="linear",yscale="linear",xlabel="t [s]",ylable="a(t)",title="Universe 616")
    fr.ax.xaxis.label.set_size(20)
    fr.ax.yaxis.label.set_size(20)
    fr.ax.tick_params(labelsize=20)
    handles, labels = fr.ax.get_legend_handles_labels()
    fr.ax.legend(handles, labels, loc="best", prop={'size': 20})
    fr.pyplt.show()
def pr4():
    dst = PL.dataset()
    ds = PL.dataset()
    dst.label=r"$a=\left(\frac{\Omega_{M}}{\Omega_{\Lambda}}\right)^\frac{1}{3} \left(\sinh(\frac{t}{t_{\Lambda}})\right)^\frac{2}{3} $ with $t_{\Lambda}$ = 3.5e17 "
    ds.label="numerical"

    fu = FU.Friedmann_Universe()
    fu.omega_M=0.29
    fu.omega_R=5e-5
    fu.omega_lambda=0.71
    a,t2 = fu.solveFora2()
    t2=np.array(t2)
    t2 = t2 + max(-t2)
    t2 = t2[-5000:]
    a = a[-5000:]
    t=np.logspace(np.log10(min(t2[t2!=0])),np.log10(max(t2)),100)

    y=testpr3(t,0.29,0.71)
    t2 = t2 / 3.154e+7
    t = t / 3.154e+7
    dst.x = t
    for i in range(len(y)):
        if y[i]>1e1:
            y[i]=1
    dst.y = y
    # t2 = np.append(t2, [t2[-1]])
    # a = np.append(a, [0])
    ds.x = t2
    ds.y = a

    pl = PL.Plotter()
    fr = pl.Plot([ds,dst],xscale="log",yscale="log",xlabel="t [yr]",ylable="a(t)",title="Universe 616")
    fr.ax.xaxis.label.set_size(20)
    fr.ax.yaxis.label.set_size(20)
    fr.ax.tick_params(labelsize=20)
    handles, labels = fr.ax.get_legend_handles_labels()
    fr.ax.legend(handles, labels, loc="best", prop={'size': 20})
    fr.pyplt.show()
pr4()
