# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:11:09 2019

@author: Batuhan Özdöl 150180701
"""

import numpy as np
from scipy.integrate import quad
#for the (a) when m != n, m and n is int
def integranda(m,n,f,t):
    return np.sin(2*np.pi*m*f*t)*np.sin(2*np.pi*n*f*t)

f=1
m=2
n=4
L=np.pi   # -L<=t<=L
ans1,err = quad(integranda,-1*L,L,args=(m,n,f))
print("Result (a)= %.1f ->orthogonal"% (ans1))

#for the (b) when m != n, m and n is int
def integrandb(m,n,f,t):
    return np.cos(2*np.pi*m*f*t)*np.cos(2*np.pi*n*f*t)

f=1
m=1
n=3
L=np.pi   # -L<=t<=L
ans2,err = quad(integrandb,-1*L,L,args=(m,n,f))
print("Result (b)= %.1f ->orthogonal"% (ans2/2))

#for the (c) when m != n, m and n is int
def integrandc(m,n,f,t):
    return np.sin(2*np.pi*n*f*t)*np.cos(2*np.pi*m*f*t)

f=1
m=2
n=5
L=np.pi   # -L<=t<=L
ans3,err = quad(integrandc,-1*L,L,args=(m,n,f))
print("Result (c)= %.1f ->orthogonal"% (ans3))
        
#for exp x degrees, n terms
def taylore(x,n):
    e=0
    for i in range(n):
        y=x*math.pi/180
        e+=y**i/math.factorial(i)
    return e
#for the (d) when m != n, m and n is int
# it will give the result but also ComplexWarning 
def integrandd(m,n,f,t):
        return np.exp((0+1j)*2*np.pi*n*f*t/np.pi)*np.exp((0+1j)*2*np.pi*m*f*t/np.pi)
f=1
m=2
n=5
ans4,err = quad(integrandd,0,np.pi,args=(m,n,f))
print("Result (d)= %.1f ->orthogonal"% (abs(ans4)))





