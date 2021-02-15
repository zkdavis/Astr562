import numpy as np
import need_cons as nc
import need_plots as NP


pl = NP.Plotter()
colors = pl.colors
def bern_eq(r,v,m_dot,gam=4/3):
    rho = m_dot/(4*np.pi*(r**2)*v)
    f=0.5*(v**2) + ((rho**(gam-1)) - 1)/(gam - 1) - (1/r)
    return f

v = np.linspace(0,3,1001)
r1 = np.linspace(-3,0,500)
r2 = np.linspace(0,3,5000)
mds=[0.1,1,2,4,8,10,20]
dss=[]
for md in mds:
    print(md)
    ds = NP.dataset()
    ds2 = NP.dataset()
    x_temp=[]
    y_tmep=[]
    x1_temp=[]
    y1_tmep=[]
    for vi in v:
       for ri in r1:
           tval = bern_eq(ri,vi,md)
           #print(tval)
           if(np.abs(tval)<9e-3):
               x_temp.append(ri)
               y_tmep.append(vi)

    for vi in v:
       for ri in r2:
           tval = bern_eq(ri,vi,md)
           #print(tval)
           if(np.abs(tval)<5e-4):
               x1_temp.append(ri)
               y1_tmep.append(vi)

    tempx=[]
    tempy=[]
    for i in range(len(y1_tmep)):
        if(y1_tmep[i]>0.001):
            tempy.append(y1_tmep[i])
            tempx.append(x1_temp[i])
    y1_tmep=tempy
    x1_temp=tempx
    ds.x=x_temp
    ds.y=y_tmep

    ds.color=next(colors)
    ds.label="$\dot{m}=$"+str(md)
    ds.marker_size=6
    ds2.marker_size=6
    ds2.x = x1_temp
    ds2.y = y1_tmep
    ds2.color = ds.color
    ds2.plot_type = ds.scattertype
    ds.plot_type = ds.scattertype
    dss+=[ds,ds2]
dsxax = NP.dataset()
dsyax = NP.dataset()
dsxax.x = list(np.linspace(-5,5,100))
dsxax.plot_type=dsxax.plottype
dsxax.color='r'
dsyax.color='r'
dsxax.marker='-'
dsyax.marker='-'
dsxax.y = [0]*len(dsxax.x)
dsyax.y = list(np.linspace(-1,5,100))
dsyax.plot_type=dsxax.plottype
dsyax.x = [0]*len(dsyax.y)
dss+=[dsxax,dsyax]
fr = pl.Plot(datasets=dss,xscale='linear',yscale='linear',minx=-3,maxx=3,miny=-1,maxy=3,ylable="v",xlabel="r",title="V vs r")
fr.pyplt.show()