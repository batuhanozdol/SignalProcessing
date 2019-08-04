# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 11:40:16 2019

@author: CEM
"""
import numpy
from scipy.io import wavfile

fs, data = wavfile.read('input.wav')
for i in range(len(a)):
    b.append(0)
c=a[0]*np.roll(b,0)
for i in range(1,len(a)):
    c+=a[i]*np.roll(b,i)
print(c)