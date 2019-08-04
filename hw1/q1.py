# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:20:24 2019

@author: Batuhan Özdöl 150180701
"""

#  Taylor Expansion for sine
import math
import numpy as np

#for sine x degrees, n terms
def taylorsin(x,n):
    sin=0
    for i in range(n):
        sign=(-1)**i
        y=x*(math.pi/180)
        sin+=sign*y**(2*i+1)/math.factorial(2*i+1)
    return sin
#for cosine x degrees, n terms
def taylorcos(x,n):
    cos=0
    for i in range(n):
        sign=(-1)**i
        y=x*(math.pi/180)
        cos+=sign*y**(2*i)/math.factorial(2*i)
    return cos
#for exp x degrees, n terms
def taylore(x,n):
    e=0
    for i in range(n):
        y=x*math.pi/180
        e+=y**i/math.factorial(i)
    return e
# θ = 30 
e=taylore(30*complex(0,1),20)
sin=taylorsin(30,20)
cos=taylorcos(30,20)
result=cos+complex(0,1)*sin
print("e**(30j)=%s"% e)
print("cos(30)+jsin(30)=%s"% result)

