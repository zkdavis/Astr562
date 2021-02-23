import numpy as np
from ModelFitter import dataform as df
from ModelFitter import Fitter
from need_plots import dataset,figret
import need_plots
import problem3and4 as pp
import need_cons as nc
import data_reader as dr
import time


class compare_data:
    def __init__(self,data_d,data_z,data_file):
        self.data_d=data_d
        self.data_z = data_z
        self.data_file = data_file
        self.name = str(self.data_file).split(".")[0]

class tgf:
    def __init__(self):
        print('asdf')
        self.stuff = pp.p4()



    def getYandX(self,T0, x0) -> dataset:

        ds = dataset()
        t=np.linspace(0, 60, 300)
        y=[]
        ds.x=t
        self.stuff.x0=x0
        for i in t:
            y.append(self.stuff.L_out(self.stuff.L_heat_ni_co_simplified, i, T0))
        ds.y = y
        ds.plot_type=ds.plottype
        return ds
    def getCompareData(self) -> dataset:
        dt = dr.getdata()
        tx = dt[0]
        ty = dt[1]
        tty = []
        stop=100
        tx = tx[:stop]
        for i in ty[:stop]:
            tty.append(nc.MBtolum(i))
        ds = dataset()
        ds.y = list(tty)
        ds.x = list(tx)
        return ds

    def run(self):
        t = np.linspace(0, 300, 100)
        y = []
        k = 0.4
        m = nc.solar_M
        v = 1e7
        tt = np.sqrt(k * m / (v ** 2))
        tt = nc.sec2day(tt)*1e-4
        T0 = df(tt,tt*1e-2 + 1,tt*1e2,1,"T0")
        x0=df(9e36,5e36,1e37,1,"x0")
        cds = self.getCompareData()
        ds = self.getYandX(T0.data, x0.data)
        ds.plot_type=ds.plottype

        pl=need_plots.Plotter()
        fr = pl.Plot([ds],xscale="linear",yscale="linear")
        fargs = [T0, x0]
        mf = Fitter(func=self.getYandX,ds=cds,figret=fr,fargs=fargs,max_int=1000,show_error=False)
        return mf


tbf = tgf()
fit = tbf.run()
