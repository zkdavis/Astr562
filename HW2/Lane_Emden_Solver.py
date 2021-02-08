import numpy as np
import Runga_Kutta as RK
import need_plots as PL



class LESolver:
    def __init__(self,n=None,gamma=5/3,xmax=50,xmin=0,theta_0=1):
        if(n==None):
            self.gamma = gamma
            self.n = 1 / (self.gamma - 1)
        else:

            self.n = n
            if(self.n==0):
                self.gamma=0
            else:
                self.gamma = (1/self.n) + 1
        self.x_max = xmax
        self.x_min =xmin
        self.x_num = 1000 * self.x_max
        self.x = np.linspace(self.x_min, self.x_max, self.x_num+1)
        self.theta_0 = theta_0
        self.omega_0 = 0
        self.theta = np.zeros_like(self.x)
        self.omega = np.zeros_like(self.theta)

    def dw_dx(self, x_i: float, omega_i: float, i: int):
        f = -(x_i ** 2) * (self.theta[i] ** self.n)
        # if(np.isnan(f)):
        #     print("nan?")
        return f


    def dtheta_dx(self,x_i: float, theta_i: float, i: int):
        if(x_i == 0 ):
            f=0
        else:
            f = self.omega[i] / (x_i ** 2)
        return f


    def solve(self):
        self.theta[0] = self.theta_0
        self.omega[0] = self.omega_0
        for i in range(len(self.theta)-1):
            self.omega[i] = RK.iteration(self.dw_dx, self.x, self.omega, i, order=4)[i]
            self.theta[i] = RK.iteration(self.dtheta_dx, self.x, self.theta, i, order=4)[i]



    def theta_n_0(self,x: iter):
        f = 1 - (1 / 6) * (x ** 2)
        return f


    def theta_n_1(self,x: iter):
        f = np.sin(x) / x
        return f


    def theta_n_5(self,x: iter):
        f = 1 / np.sqrt(1 + ((x ** 2) / 3))
        return f



