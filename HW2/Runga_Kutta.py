import numpy as np


def iteration(f, x: iter, y: iter, i: int, order: int = 4) -> iter:
    #dy/dt = f(t,y)
    #dx = np.abs(x[i+1]-x[i])
    dx = x[i + 1] - x[i]
    ty = y[i]
    k1 = f(x[i],y[i],i)
    k2 = f(x[i] + dx/2,y[i] + dx*k1/2,i)
    k3 = f(x[i] + dx/2,y[i] + dx*k2/2,i)
    k4 = f(x[i] + dx,y[i] + dx*k3,i)
    if(order == 4):
        tval = (dx/6)*(k1 + 2*k2 + 2*k3 + k4)
        # if np.isnan(tval):
        #     print("nan?")
        if(len(y)>(i+1)):
            y[i+1] = y[i] + tval
        else:
            y= np.append(y,[y[i]+tval])
            #y.append(y[i] + tval)
    else:
        if (len(y) > (i + 1)):
            y[i + 1] = y[i] + dx * k2
        else:
            y.append(y[i] + dx * k2)

    return y

def solve(f,x:iter,y:iter,order:int=4) -> iter:
    for i in range(len(y)-1):
        y = iteration(f,x,y,i,order)
    return y