import os

def getdata():
    x=[]
    y=[]
    file="sn2011fe.dat"
    f = open(file, "r")
    for l in f:
        spl = l.split(" ")
        tx = spl[0]
        ty= spl[1]
        x.append(float(tx))
        y.append(float(ty))
    return x,y

