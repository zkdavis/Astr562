from decimal import Decimal

from astropy import constants as const

c_light = const.c.cgs.value
h_bar = const.hbar.cgs.value
h = const.h.cgs.value
me = const.m_e.cgs.value
mp = const.m_p.cgs.value
G = const.G.cgs.value
solar_M = const.M_sun.cgs.value
k_boltz = const.k_B.cgs.value
L_solar = const.L_sun.cgs.value
sig_sb = const.sigma_sb.cgs.value

def ev2ergs(ev):
    return ev/6.242e+11
def solarMtoCGS(M):
    return M*solar_M
def parsec2cm(parsec):
    return parsec*3.086e18
def cm2parsec(cm):
    return cm/3.086e18
def sec2min(s):
    return s/60
def sec2hour(s):
    return sec2min(s)/60
def sec2day(s):
    return sec2hour(s)/24
def sec2year(s):
    return sec2day(s)/365
def min2sec(s):
    return s*60
def hour2sec(h):
    return min2sec(60)*h
def day2sec(d):
    return hour2sec(24)*d
def year2sec(s):
    return day2sec(365)*s

def num2science(n):
    a = '%E' % n
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

def arcsec2deg(arcsec):
    return arcsec/(3600)
def lightyears2cgs(ly):
    return 9.461e+17*ly

def MBtolum(mb):
    L0=3.0128e35
    L = L0*(10**(-0.4*mb))
    return L

def AU2cm(au):
    return 1.496e+13*au