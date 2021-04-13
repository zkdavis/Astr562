from HW2 import Runga_Kutta as RK
import numpy as np
import need_cons as nc

class Friedmann_Universe():
    def __init__(self):
        self.H_0 = 70*1e5/(nc.parsec2cm(1)*1e9)
        self.dtm = 5e-2
        self.dt = self.dtm/self.H_0
        self.omega_M=1
        self.omega_R=0
        self.omega_K=0
        self.omega_lambda=0

    def Friedmann_equation(self,null1,a,null2):
        #returns H(a)
        if(a != 0):
            print(a)
            f = self.H_0*np.sqrt(self.omega_lambda + (self.omega_M/(a**3)) + (self.omega_R/(a**4)) + (self.omega_K/(a**2)))
        else:
            f=0
        return f

    def Friedmann_equation_u(self,null1,u,null2):
        #returns H(u)
        if(u != 0):
            print(u)
            f = self.H_0*np.sqrt(self.omega_lambda + (self.omega_M/(10**(3*u))) + (self.omega_R/(10**(4*u))) + (self.omega_K/(10**(2*u))))
        else:
            f=self.H_0*np.sqrt(self.omega_lambda + (self.omega_M/(10**(3*u))) + (self.omega_R/(10**(4*u))) + (self.omega_K/(10**(2*u))))
        return f

    def solveForU(self,dt=1e1,maxu=1e50):
        #solves for U=log10(a)
        #solves from now to beginning ie a(t_initial) = 1 a(t_final)=0
        y=[0]
        t=[0]
        f = self.Friedmann_equation_u
        i=0
        while(y[-1]>(-maxu) and i<50000):
            t.append(t[i]- (dt/(i+1)))
            y = RK.iteration(f,t,y,i)
            i+=1
        return y,t

    def solveFora(self,maxu=1e100):
        dt = self.dt
        u,t = self.solveForU(dt,maxu)
        a = 10**(np.array(u))
        return a,t


