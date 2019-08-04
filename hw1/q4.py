# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:37:04 2019

@author: Batuhan Özdöl 150180701
"""
import numpy as np
import matplotlib.pyplot as plt
# function for (a) cos^2(2πt) to check is it perodic func. 
def isaperiodic(t):
    if(np.cos(2*np.pi*t)**2==np.cos(2*np.pi*t+2*np.pi)**2):
        print("(a) is periodic")
        return
    else:
        print("(a) is not periodic")
        return
#for cos^2(2πt) in (a)
isaperiodic(60)

#function for (b) that checks e^jπt
def isbperiodic(t):
    if(np.cos(np.pi*t)==np.cos(np.pi*t+2*np.pi) and round(np.sin(np.pi*t),10)==round(np.sin(np.pi*t+2*np.pi),10)):
        print("(b) is periodic")
        return
    else:
        print("(b) is not periodic")
        return
# t=30 for e^jπt
isbperiodic(30)

# for (c) 1 + 5cos(2257πt + π/4) + 2cos(2440πt + 3π/2)
def iscperiodic(t):
    if(1+5*(np.cos(2257*np.pi*t)+2*np.cos(2440*np.pi*t+3*np.pi/2)) == 1+5*(np.cos(2257*np.pi*t+2*np.pi)+2*np.cos((2440*np.pi*t+3*np.pi/2)+2*np.pi))):
        print("(c) is periodic")
        return
    else:
        print("(c) is not periodic")
        return
# checking 1 + 5cos(2257πt + π/4) + 2cos(2440πt + 3π/2) t=120 for is it periodic
iscperiodic(120)

time = np.arange(-5*np.pi,5*np.pi,0.2)
#for the (a) = cos^2(2πt)
f1=np.cos(2*time)*np.cos(2*time)
plt.plot(time,f1)
plt.title("(a)= cos^2(2πt) signal")
plt.xlabel("time")
plt.show()
#for the (b) = e^jπt
f2=np.exp((0+1j)*time)
plt.plot(time,f2)
plt.title("(b)= e^jπt signal")
plt.xlabel("time")
plt.show()
# for (c) 1 + 5cos(2257πt + π/4) + 2cos(2440πt + 3π/2)
f3=1+5*np.cos(2257*time+np.pi/4)+2*np.cos(2440*time+3*np.pi/2)
plt.plot(time,f3)
plt.title("(c)= 1 + 5cos(2257πt + π/4) + 2cos(2440πt + 3π/2) signal")
plt.xlabel("time")
plt.show()

#magnitude spectrum of cos^2(2πt) f=1Hz
plt.magnitude_spectrum(f1,Fs=1)
plt.title("Magnitude spectrum of cos^2(2πt)")
plt.show()
#magnitude spectrum of e^jπt f=0.5Hz
plt.magnitude_spectrum(f2,Fs=1/2)
plt.title("Magnitude spectrum of e^jπt")
plt.show()
#magnitude spectrum of 1 + 5cos(2257πt + π/4) + 2cos(2440πt + 3π/2) f=30.5
plt.magnitude_spectrum(f3,Fs=30.5)
plt.title("Magnitude spectrum of 1 + 5cos(2257πt + π/4) + 2cos(2440πt + 3π/2)")
plt.show()



