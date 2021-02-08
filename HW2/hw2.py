import numpy as np
import Lane_Emden_Solver as LES
import need_plots as PL
import need_cons as con

def part_a(n):
    les = LES.LESolver(n=n)
    les.solve()
    pl = PL.Plotter()
    datasets = []
    ds1 = PL.dataset()
    cf = None
    ds1.x = les.x
    if (les.n == 0):
        cf = les.theta_n_0(ds1.x)
    elif (les.n == 1):
        cf = les.theta_n_1(ds1.x)
    elif (les.n == 5):
        cf = les.theta_n_5(ds1.x)
    ds1.label = "Analytical Solution for n=" + str(les.n)
    newy=[]
    newx=[]
    if(cf is not None):
        for ii in range(len(cf)):
            if(ii%1000==0):
                newy.append(cf[ii])
                newx.append(ds1.x[ii])
    ds1.y = newy
    ds1.x = newx
    ds1.plot_type=PL.dataset.scattertype
    ds2 = PL.dataset()
    ds2.x = les.x
    ds2.y = les.theta
    ds2.plot_type=PL.dataset.plottype
    ds2.color = 'y'
    ds2.label = "Runge kutta dx=" + str(np.abs(les.x[1] - les.x[0]))
    if (cf is not None):
        datasets.append(ds1)
    datasets.append(ds2)
    figret = pl.Plot(datasets=datasets, xscale='linear', yscale='linear',ylable=r"$\theta$",xlabel="x",title="Lane-Emden Solution for n="+str(n))
    figret.pyplt.savefig("problem1an="+str(n))


def part_b():
    gamma=5/3
    les = LES.LESolver(gamma=gamma)
    les.solve()
    artemp = les.theta
    artemp = np.abs(artemp)
    min = np.nanargmin(artemp)
    x0 = les.x[min]
    print("x0: " + str(x0))

def part_c(solar_m):
    gamma = 5 / 3
    les = LES.LESolver(gamma=gamma)
    les.solve()
    artemp = les.theta
    artemp = np.abs(artemp)
    minv = 0
    for i in range(len(les.theta)):
        if (les.theta[i] >= 0):
            if (les.theta[i] < les.theta[minv]):
                minv = i
        else:
            break
    min = minv
    t1 = artemp[min]
    t2 = les.theta[min]
    x0 = les.x[min]
    thetan = les.theta ** les.n
    I1 = np.trapz(thetan[:min] * (les.x[:min] ** 2), x=les.x[:min])
    k = (con.h_bar ** 2) / (con.me * (con.mp ** (5 / 3)))
    beta = (3 / (2 * les.n)) - 0.5
    m = con.solarMtoCGS(solar_m)
    dem = 4 * np.pi * I1 * ((((les.n + 1) / (4 * np.pi * con.G)) * k) ** (3 / 2))
    rho_c = (m / dem) ** (1 / beta)

    print("rho_c: "+str(rho_c))

def part_d(solar_m):
    gamma = 5 / 3
    les = LES.LESolver(gamma=gamma)
    les.solve()
    artemp = les.theta
    artemp = np.abs(artemp)
    minv =0
    for i in range(len(les.theta)):
        if(les.theta[i]>=0):
            if(les.theta[i]<les.theta[minv]):
                minv=i
        else:
            break
    min=minv
    t1 = artemp[min]
    t2 = les.theta[min]
    x0 = les.x[min]
    thetan=les.theta**les.n
    I1 = np.trapz(thetan[:min]*(les.x[:min]**2),x=les.x[:min])
    k = (con.h_bar**2)/(con.me * (con.mp**(5/3)))
    beta = (3/(2*les.n)) - 0.5
    m = con.solarMtoCGS(solar_m)
    dem = 4 * np.pi * I1* ((((les.n+1)/(4*np.pi*con.G))*k)**(3/2))
    rho_c = (m/dem)**(1/beta)
    R0 = (((les.n+1)/(4*np.pi*con.G))*k*(rho_c**((1/les.n)-1)))**(1/2)
    R=R0*x0
    print("R: " + str(R))

part_d(1)
#part_c(1)
#part_b()
#part_a(1)
