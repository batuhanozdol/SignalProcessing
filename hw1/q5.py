# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 10:57:48 2019

@author: Batuhan Özdöl 150180701
"""
import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt

f1 = 1100 #1100 Hz
f2 = 1099 #1099 Hz
f3 = 1100 #1100 Hz
f4 = 1094 #1094 Hz

T = 10 #10 sec

time = np.arange(0,T,0.001) # 10sec long time range

#signal is sin(2*pi*f*t)
x1=np.sin(2*time*f1*np.pi)
x2=np.sin(2*time*f2*np.pi)
firstsig=(x1+x2)/2
plt.plot(time,firstsig)
plt.title("First signal")
plt.xlabel("time")
plt.show()

#writing first signal with 5000 sampling rate= 5000samples/sec
scipy.io.wavfile.write("firstwave.wav",5000,firstsig)


x3=np.sin(2*f3*time*np.pi)
x4=np.sin(2*f4*time*np.pi)
secondsig=(x3+x4)/2
plt.plot(time,secondsig)
plt.title("Second signal")
plt.xlabel("time")
plt.show()

#writing second signal with 5000 sampling rate= 5000samples/sec
scipy.io.wavfile.write("secondwave.wav",5000,secondsig)




