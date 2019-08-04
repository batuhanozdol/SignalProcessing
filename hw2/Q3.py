# -*- coding: utf-8 -*-

import numpy as np
from scipy.io import wavfile

fs1, data1 = wavfile.read("input.wav")
fs2, data2 = wavfile.read("h1.wav")
fs3, data3 = wavfile.read("h2.wav")
fs4, data4 = wavfile.read("h3.wav")

left1 = data1[:,0]
right1 = data1[:,1]
left2 = data2[:,0]
right2 = data2[:,1]
left3 = data3[:,0]
right3 = data3[:,1]
left4 = data4[:,0]
right4 = data4[:,1]

# determined data1=x[n] , data2=h[n]
def convol(data1,data2):
    # up to 0 added numbers to shifting number of h[n]
    for i in range(len(data1)):
        data2=np.append(data2,0)
    # first defined y[0]=x[0]*h[0]
    y=data1[0]*np.roll(data2,0)
    for i in range(1,len(data1)):
        # if x[n] is not 0 we will find x[n]*h[n]
        if data1[i]!= 0:
            y+=data1[i]*np.roll(data2,i)
    return y

# finding convolution of right and left channels for each output file
l1 = convol(left1,left2)
r1 = convol(right1,right2)
l2 = convol(left1,left3)
r2 = convol(right1,right3)
l3 = convol(left1,left4)
r3 = convol(right1,right4)

wavfile.write("y1.wav",fs1,np.column_stack((l1,r1)).ravel().astype(np.int16))
wavfile.write("y2.wav",fs1,np.column_stack((l2,r2)).ravel().astype(np.int16))
wavfile.write("y3.wav",fs1,np.column_stack((l3,r3)).ravel().astype(np.int16))






