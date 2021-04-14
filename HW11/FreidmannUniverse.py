from HW2 import Runga_Kutta as RK
import numpy as np
import need_cons as nc
import math

class Friedmann_Universe():
    def __init__(self):
        self.H_0 = 70*1e5/(nc.parsec2cm(1)*1e6)
        #self.H_0 =1 #70*1e5/(nc.parsec2cm(1)*1e9)
        self.dtm = 5e-4
        self.dt = self.dtm/self.H_0
        self.omega_M=1
        self.omega_R=0
        self.omega_K=0
        self.omega_lambda=0
        self.al0 = False

    def Friedmann_equation(self,null1,a,null2):
        #returns H(a)
        if(a != 0):
            print(a)
            if(a<0 or math.isnan(a) or math.isinf(a)):
                self.al0 =True
            else:
                self.al0 = False
            f = self.H_0*np.sqrt(self.omega_lambda + (self.omega_M/(a**3)) + (self.omega_R/(a**4)) + (self.omega_K/(a**2)))
        else:
            f=0
        return f

    def Friedmann_equation2(self,null1,a,null2):
        #returns H(a)
        if(a != 0):
            print(a)
            print(a)
            if (a < 0 or math.isnan(a) or math.isinf(a)):
                self.al0 = True
            else:
                self.al0 = False
            f = self.H_0*np.sqrt((self.omega_lambda*(a**2)) + (self.omega_M*(a**-1)) + (self.omega_R*(a**-2)) + (self.omega_K))
            if(math.isnan(f)):
                print("afds")
        else:
            print("a=0000")
            f=0
        return f

    def Friedmann_equation_u(self,null1,u,null2):
        #returns H(u)
        #f = self.H_0*np.sqrt(self.omega_lambda + (self.omega_M*np.exp(-3*u)) + (self.omega_R*np.exp(-4*u)) + (self.omega_K*np.exp(-4*u)))
        f = self.H_0*np.sqrt((self.omega_M*np.exp(-3*u)))
        return f
    def Friedmann_equation_u2(self,u):
        #returns H(u)
        f = self.H_0*np.sqrt(self.omega_lambda + (self.omega_M*np.exp(-3*u)) + (self.omega_R*np.exp(-4*u)) + (self.omega_K*np.exp(-4*u)))
        return f
    def solveForU(self,dt=1e1,maxu=1e50):
        #solves for U=log10(a)
        #solves from now to beginning ie a(t_initial) = 1 a(t_final)=0
        y=np.array([0],dtype=np.float64)
        t=np.array([0],dtype=np.float64)
        f = self.Friedmann_equation_u
        i=0
        if(y[-1]<=(-maxu)):
            print("gmaxu")
        while(y[-1]>(-maxu) and i<1000):
            dt = dt
            if(len(t)>2):
                dt = np.log(np.abs(t[i])/np.abs(t[i-1]))
            t = np.append(t,[t[i]- (dt)])
            y = RK.iteration(f,t,y,i)

            i+=1
        return y,t

    def solveFora(self,maxu=1e1):
        dt = self.dt
        u,t = self.solveForU(dt,maxu)
        a = np.exp(np.array(u))
        return a,t

    def solveFora2(self,mina=9e-10):
        # solves from now to beginning ie a(t_initial) = 1 a(t_final)=0
        dt = self.dt
        y = np.array([1], dtype=np.float64)
        t = np.array([0], dtype=np.float64)
        f = self.Friedmann_equation2
        i = 0
        j=1
        if (y[-1] <= mina):
            print("lmina")
        while (y[-1] > mina and i < 1000000):
            if(y[-1]<0.1 and j<2):
                j+=1
                dt = dt/100
            if (y[-1] < 0.001 and j < 3):
                j += 1
                dt = dt / 1000
            if (y[-1] < 1e-5 and j < 3):
                j += 1
                dt = dt / 100000
            if (y[-1] < 1e-6 and j < 3):
                j += 1
                dt = dt / 10000000

            t = np.append(t, [t[i] - (dt)])
            y = RK.iteration(f, t, y, i)
            while(self.al0 is True):
                t = np.delete(t,-1)
                dt = dt/10
                t = np.append(t, [t[i] - (dt)])
                y = np.delete(y,-1)
                y = RK.iteration(f, t, y, i)
            i += 1
        return y, t


