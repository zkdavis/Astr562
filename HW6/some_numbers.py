import numpy as np
import  need_cons as nc
import need_plots as PL
#1a-d
# f=1e-9
G = nc.G
c = nc.c_light
# # m =10*nc.solar_M
# m=(c**3)/(G*f)
# rs =G*m/(c**2)
# h = 1e-13
# d = (((G*m)**(5/6))*(f**(-2/3))/(h*c))**(2/3)
# #d=rs/h
# d=nc.cm2parsec(d)
# a=(G*m/(f**2))**(1/3)
# check = rs/a
# #
# print("rs: "+ str(nc.num2science(nc.cm2parsec(rs))))
# print("a: "+ str(nc.num2science(nc.cm2parsec(a))))
# print("d: " + nc.num2science(d))
# print(nc.num2science(m/nc.solar_M))
#1 e
# m = 10*nc.solar_M
# w=1e3
# h = 1e-24
# rs =2*G*m/(c**2)
# a = (G*m/(w**2))**(1/3)
#
# print("rs: " + nc.num2science(rs))
# print("a: " + nc.num2science(a))

#1f
# def limitthing(h,f):
#     return (h**2)*(f**2)*1e34
# hligo=1e-24
# fligo=1e3
# hlisa = 1e-21
# flisa = 1e-2
# hpta = 1e-13
# fpta = 1e-9
#
# print("ligo lim:" + str(limitthing(hligo,fligo)))
# print("lisa lim:" + str(limitthing(hlisa,flisa)))
# print("lipta lim:" + str(limitthing(hpta,fpta)))
# #1g
# def strain(m,f,r):
#     h = (((G*m)**(5/6))*(f**(-2/3)))/(c*(r**(3/2)))
#     return h
# def rs(m):
#     return 2*G*m/(c**2)
# def cutoff(m,fr,h):
#     for i in range(len(fr)):
#         a=(G*m/(fr[i]**2))**(1/3)
#         ss = rs(m)
#         if(a<=ss):
#             h[i]=0
#     return h
#
#
# f=np.logspace(-10,3,1000)
# m_neutron=nc.solar_M
# m_wd = 10*nc.solar_M
# m_smbh = 1e9*nc.solar_M
# d=nc.parsec2cm(1e10)
# h_neutron = strain(m_neutron,f,d)
# h_neutron = cutoff(m_neutron,f,h_neutron)
# h_wd = strain(m_wd,f,d)
# h_wd = cutoff(m_wd,f,h_wd)
# h_smbh = strain(m_smbh,f,d)
# h_smbh = cutoff(m_smbh,f,h_smbh)
# hligo=1e-24
# fligo=1e3
# hlisa = 1e-21
# flisa = 1e-2
# hpta = 1e-13
# fpta = 1e-9
# pl = PL.Plotter()
# ds = PL.dataset()
# ds.label="Neutron Star"
# ds.plot_type = ds.plottype
# ds2 = PL.dataset()
# ds2.label = "White dwarf"
# ds3 = PL.dataset()
# ds3.plot_type = ds.plottype
# ds2.plot_type = ds.plottype
# ds4 = PL.dataset()
# ds5 = PL.dataset()
# ds6 = PL.dataset()
# ds4.x = [fligo]
# ds4.y = [hligo]
# ds5.x = [flisa]
# ds5.y = [hlisa]
# ds6.x = [fpta]
# ds6.y = [hpta]
# ds4.label="LIGO"
# ds5.label="LISA"
# ds6.label="PTA"
# ds3.label = "SMBH"
# ds.x = f
# ds.y = h_neutron
# ds2.x = f
# ds2.y = h_wd
# ds3.x = f
# ds3.y = h_smbh
# figret = pl.Plot([ds,ds2,ds3,ds4,ds5,ds6],xlabel="f [Hz]",ylable="h",title="")
# figret.pyplt.show()

#2c

# def rs(m):
#     return 2*G*m/(c**2)
#
# def strain_t(m,r,t):
#     ss = rs(m)
#     tm=1e2*ss/c
#     f = ((G*m)**(1/2))*(ss*((tm-t)**(1/4)))/(c*(r**(3/2)))
#     phi=np.sin((((c/ss)*(tm-t))**(5/8)))
#     return f*phi
# m=nc.solar_M
# ss = rs(m)
# tm=1e2*ss/c
# t = np.linspace(0,tm,1000)
# ds = PL.dataset()
# ds.x=t
# ds.y = strain_t(m,1e18,t)
# pl = PL.Plotter()
# figret = pl.Plot([ds],xscale="linear",yscale="linear")
# figret.pyplt.show()
#
#
#
#3c
def f1(f):
    return 1e-27*f
def f2(f):
    return 1e-25*((f)**1/3)
def f3(f):
    return 1e-23*((f)**-2/3)

ff = np.logspace(-5,5,1000)
ds1 = PL.dataset()
ds2 = PL.dataset()
ds3 = PL.dataset()
ds1.label="Stellar"
ds2.label="Disk"
ds3.label="stochastic background"
ds1.plot_type=ds1.plottype
ds2.plot_type=ds1.plottype
ds3.plot_type=ds1.plottype
ds1.x=ff
ds1.y=ff*(1e-27)
ds2.x=ff
ds2.y=f2(ff)
ds3.x=ff
ds3.y=f3(ff)
pl = PL.Plotter()
figret = pl.Plot([ds1,ds2,ds3],xlabel="f [Hz]",ylable="h",title="")
figret.pyplt.show()