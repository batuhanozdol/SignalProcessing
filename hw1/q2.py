# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 15:48:04 2019

@author: Batuhan Özdöl 150180701
"""
import cmath
import math

# finding n.degree roots for z with given its angle
def findingroot(z,angle,n):
    roots=[]
    length=math.sqrt((z.imag**2)+z.real**2)
    for i in range(0,n):
        x=(((angle*math.pi/180)+2*i*math.pi)/n)
        root=complex((length**(1/n))*round(math.cos(x),15),(length**(1/n))*round(math.sin(x),15))
        roots.append(root)
    return roots

# a) z= -8*(2**(1/2))+8*(2**(1/2))j
a = complex(-8*cmath.sqrt(2),8*cmath.sqrt(2))
# b) z=j
b = complex(0,1)

#for the a) we will see cube roots of a
print("Cube roots of (a) \n%s\n" % findingroot(a,135,3))

#for the b) we will see fourth roots of b
print("Fourth roots of (b) \n%s" % findingroot(b,90,4))
