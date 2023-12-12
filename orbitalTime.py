import numpy as np
rho = 1
Cd = 2.2
A = 0.04
m = 1
H = 800*10**3
EarthR=6371000
a = EarthR+H
EarthMass = 5.9722*10**24
GravConst = 6.67*10**-11
secondsInYear = 3.154*10**7
secondsInMonth = 2.628*10**6
secondsInWeek = 604800
secondsInDay = 86400
secondsInHour = 3600
secondsInMinutes = 60
totalTime = 0
def calc_period(G, M, a):
    T = 2*np.pi*np.sqrt(a**3/(G*M))
    return T

def density(a, EarthR):
    rho=0
    if((a-EarthR)>850000 and (a-EarthR)<901000):
        rho = 4.68*10**-15
    if((a-EarthR)>800000 and (a-EarthR)<851000):
        rho = 6.47*10**-15
    if((a-EarthR)>750000 and (a-EarthR)<801000):
        rho = 9.63*10**-15
    if((a-EarthR)>700000 and (a-EarthR)<751000):
        rho = 1.55*10**-14
    if((a-EarthR)>650000 and (a-EarthR)<701000):
        rho = 2.72*10**-14
    if((a-EarthR)>600000 and (a-EarthR)<651000):
        rho = 5.15*10**-14
    if((a-EarthR)>550000 and (a-EarthR)<601000):
        rho = 1.04*10**-13
    if((a-EarthR)>500000 and (a-EarthR)<551000):
        rho = 2.21*10**-13
    if((a-EarthR)>450000 and (a-EarthR)<501000):
        rho = 4.89*10**-13
    if((a-EarthR)>400000 and (a-EarthR)<451000):
        rho = 1.13*10**-12
    if((a-EarthR)>350000 and (a-EarthR)<401000):
        rho = 2.72*10**-12
    if((a-EarthR)>300000 and (a-EarthR)<351000):
        rho = 6.98*10**-12
    if((a-EarthR)>250000 and (a-EarthR)<301000):
        rho = 1.95*10**-11
    if((a-EarthR)>200000 and (a-EarthR)<251000):
        rho = 6.24*10**-11
    if((a-EarthR)>150000 and (a-EarthR)<201000):
        rho = 2.53*10**-10
    if((a-EarthR)>100000 and (a-EarthR)<151000):
        rho = 1.81*10**-9
    if((a-EarthR)>50000 and (a-EarthR)<101000):
        rho = 4.79*10**-7
    if((a-EarthR)>0 and (a-EarthR)<51000):
        rho = 1.2
    return rho

def a_reduction(Cd, A, m, rho, a):
    DA = 0
    DA = -2*np.pi*Cd*A/m*rho*a*a
    return DA

while a > EarthR:
    k=calc_period(GravConst, EarthMass, a)
    rho = density(a, EarthR)
    DA = a_reduction(Cd, A, m, rho, a)
    a = a+DA
    totalTime = totalTime+k

print(totalTime/secondsInYear)
print(totalTime/secondsInMonth)
print(totalTime/secondsInWeek)
print(totalTime/secondsInDay)
print(totalTime/secondsInHour)
print(totalTime/secondsInMinutes)
print(totalTime)

